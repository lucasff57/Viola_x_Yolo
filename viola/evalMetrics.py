from uteis import *
from BoundingBox import BoundingBox
from Evaluator import *
from BoundingBoxes import BoundingBoxes


def getBoundingBoxes():
    """Read txt files containing bounding boxes (ground truth and detections)."""
    import glob
    import os
    # Read ground truths
    currentPath = os.path.dirname(os.path.abspath(__file__))
    folderGT = os.path.join(currentPath,'groundtruths')
    os.chdir(folderGT)
    files = glob.glob("*.txt")
    files.sort()
    # Class representing bounding boxes (ground truths and detections)
    allBoundingBoxes = BoundingBoxes()
    # Read GT detections from txt file
    # Each line of the files in the groundtruths folder represents a ground truth bounding box (bounding boxes that a detector should detect)
    # Each value of each line is  "class_id, x, y, width, height" respectively
    # Class_id represents the class of the bounding box
    # x, y represents the most top-left coordinates of the bounding box
    # x2, y2 represents the most bottom-right coordinates of the bounding box
    for f in files:
        nameOfImage = f.replace(".txt","")
        fh1 = open(f, "r")
        for line in fh1:
            line = line.replace("\n","")
            if line.replace(' ','') == '':
                continue
            splitLine = line.split(" ")
            idClass = 'face' #class
            x = float(splitLine[0]) #confidence
            y = float(splitLine[1])
            w = float(splitLine[2])
            h = float(splitLine[3])
            bb = BoundingBox(nameOfImage,idClass,x,y,w,h,CoordinatesType.Absolute, None, BBType.GroundTruth, format=BBFormat.XYWH)
            allBoundingBoxes.addBoundingBox(bb)
        fh1.close()
    # Read detections
    folderDet = os.path.join(currentPath,'detections')
    os.chdir(folderDet)
    files = glob.glob("*.txt")
    files.sort()
    # Read detections from txt file
    # Each line of the files in the detections folder represents a detected bounding box.
    # Each value of each line is  "class_id, confidence, x, y, width, height" respectively
    # Class_id represents the class of the detected bounding box
    # Confidence represents the confidence (from 0 to 1) that this detection belongs to the class_id.
    # x, y represents the most top-left coordinates of the bounding box
    # x2, y2 represents the most bottom-right coordinates of the bounding box
    for f in files:
        # nameOfImage = f.replace("_det.txt","")
        nameOfImage = f.replace(".txt","")
        # Read detections from txt file
        fh1 = open(f, "r")
        for line in fh1:
            line = line.replace("\n","")
            if line.replace(' ','') == '':
                continue            
            splitLine = line.split(" ")
            idClass = 'face' #class
            confidence = 1 #confidence
            x = float(splitLine[0])
            y = float(splitLine[1])
            w = float(splitLine[2])
            h = float(splitLine[3])
            bb = BoundingBox(nameOfImage,idClass,x,y,w,h,CoordinatesType.Absolute, None, BBType.Detected, confidence ,format=BBFormat.XYWH)
            allBoundingBoxes.addBoundingBox(bb)
        fh1.close()
    return allBoundingBoxes
    
# Read txt files containing bounding boxes (ground truth and detections)
boundingboxes = getBoundingBoxes()

evaluator = Evaluator()


# Plot Precision x Recall curve
evaluator.PlotPrecisionRecallCurve(boundingboxes, # Object containing all bounding boxes (ground truths and detections)
                                   method= MethodAveragePrecision.ElevenPointInterpolation,
                                   IOUThreshold=0.5, # IOU threshold
                                   showAP=True, # Show Average Precision in the title of the plot
                                   showInterpolatedPrecision=False) # Don't plot the interpolated precision curve

metricsPerClass = evaluator.GetPascalVOCMetrics(boundingboxes, IOUThreshold=0.5)
print("Average precision values per class:\n")
# Loop through classes to obtain their metrics
for mc in metricsPerClass:
    # Get metric values per each class
    c = mc['class']
    precision = mc['precision']
    recall = mc['recall']
    average_precision = mc['AP']
    ipre = mc['interpolated precision']
    irec = mc['interpolated recall']
    totalPositives = mc['total positives'] 
    totalTruePositives = mc['total TP']
    totalFalsePositives = mc['total FP']
    # Print AP per class
    print('total positives: '+str(totalPositives) +', total true positives: '+ str(totalTruePositives)  +', total false positives: '+ str(totalFalsePositives))
    
    print('%s: %f' % (c, average_precision)) 