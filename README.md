EENG 645A FINAL PROJECT README
```bash


# STEP 1:  Move custom weights (LINK) into the data folder


# STEP 2:  BUILD Docker container
docker-compose up --build yolov4_cpu

# STEP 3:  RUN Docker container (all commands afterward are inside the container)
docker-compose run --rm yolov4_cpu

# STEP 4:  BUILD custom yolov4 inside container (if checkpoints/custom-416 does not exist or is empty)
python save_model.py --weights ./data/custom.weights --output ./checkpoints/custom-416 --input_size 416 --model yolov4 

# STEP 5:  EVALUATE (run each command in order)
python change_annotation_format.py
python evaluate.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --annotation_path ./data/dataset/valcustom.txt
cd /opt/project/mAP
python main.py --output results_evaluate

# STEP 6:  DETECT on all images in /opt/project/data/images.  
# Outputs ordered images in /opt/project/detections for viewing.
cd /opt/project
cd data/images
find -maxdepth 1 -type f ! -name flist.txt -printf  "./data/images/%P, " > /opt/project/flist.txt
cd /opt/project
truncate -s-2 flist.txt
python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images "$(<flist.txt)"


# Below demonstrates how to run on a video.  I don't have any videos for testing, so this is a placeholder.
# Run custom yolov4 model on video
python detect_video.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --video ./data/video/cars.mp4 --output ./detections/results.avi
```






ADDITIONAL INFORMATION (FROM THE ORIGINAL AUTHOR)

```bash
save_model.py:
  --weights: path to weights file
    (default: './data/yolov4.weights')
  --output: path to output
    (default: './checkpoints/yolov4-416')
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'False')
  --input_size: define input size of export model
    (default: 416)
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)

detect.py:
  --images: path to input images as a string with images separated by ","
    (default: './data/images/kite.jpg')
  --output: path to output folder
    (default: './detections/')
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'False')
  --weights: path to weights file
    (default: './checkpoints/yolov4-416')
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
  --size: resize images to
    (default: 416)
  --iou: iou threshold
    (default: 0.45)
  --score: confidence threshold
    (default: 0.25)
    
detect_video.py:
  --video: path to input video (use 0 for webcam)
    (default: './data/video/video.mp4')
  --output: path to output video (remember to set right codec for given format. e.g. XVID for .avi)
    (default: None)
  --output_format: codec used in VideoWriter when saving video to file
    (default: 'XVID)
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'false')
  --weights: path to weights file
    (default: './checkpoints/yolov4-416')
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
  --size: resize images to
    (default: 416)
  --iou: iou threshold
    (default: 0.45)
  --score: confidence threshold
    (default: 0.25)
```


### References

  * YOLOv4: Optimal Speed and Accuracy of Object Detection [YOLOv4](https://arxiv.org/abs/2004.10934).
  * [darknet](https://github.com/AlexeyAB/darknet)
  
   My project is inspired by these previous fantastic YOLOv3 implementations:
  * [Yolov3 tensorflow](https://github.com/YunYang1994/tensorflow-yolov3)
  * [Yolov3 tf2](https://github.com/zzh8829/yolov3-tf2)
