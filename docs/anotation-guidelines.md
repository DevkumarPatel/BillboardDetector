### Guidelines for Collecting and Annotating Images for Detecting Physical Advertisements

#### **1. Image Collection**

- **Diversity:** 
  - **Variety of Locations:** Collect images from different geographical locations, urban and rural areas.
  - **Different Times of Day:** Capture images at various times of day to include different lighting conditions.
  - **Weather Conditions:** Include images taken in different weather conditions (sunny, cloudy, rainy).

- **Classes of Advertisements:**
  - **Billboards:** Static billboards of various sizes.
  - **LED Billboards:** Electronic billboards with changing content.
  - **Bus Advertisements:** Ads displayed on the sides, back, and top of buses.
  - **Other Advertisements:** Include posters, banners, and any other physical advertisement formats.

- **Angles and Perspectives:** 
  - Capture images from multiple angles and distances.
  - Include occlusions and partially visible advertisements.

#### **2. Image Annotation**

- **Bounding Boxes:**
  - **Precision:** Draw tight bounding boxes around the advertisements, ensuring minimal background.
  - **Clarity:** Avoid cutting off parts of the advertisement or including parts of other objects.

- **Class Labels:**
  - Label each bounding box with one of the following classes:
    - `billboard`
    - `led_billboard`
    - `bus_advertisement`
    - `other_advertisement`
  - These can be added as the datasets grows bigger. 

- **Multiple Objects:**
  - Annotate each instance of an advertisement separately, even if they overlap.
  - Clearly distinguish between different advertisement types in the same image.

- **Edge Cases:**
  - Annotate small advertisements accurately.
  - Ensure large advertisements are fully covered by the bounding box, even if it spans a significant part of the image.

#### **3. Quality Control**

- **Consistency:** 
  - Follow the same annotation criteria across all images.
  - Use a predefined set of class labels without deviations.

- **Review Process:**
  - Regularly review annotations for accuracy and consistency.
  - Use peer reviews or automated tools to check for annotation quality.

#### **4. Annotation Tools**

- **Selection of Tool:**
  - Use reliable annotation tools like Roboflow, LabelImg, CVAT, or VGG Image Annotator.
  
- **Tool Configuration:**
  - Set up the tool with predefined class labels.
  - Enable features like zooming and edge detection to improve annotation accuracy.

#### **5. Metadata and Documentation**

- **Metadata:**
  - Include additional metadata like the difficulty level of detection and occlusion percentage if applicable.
  - We can also add geological metadata. 
  - Can add auxilary text information such as brand participating in the advertisements. 

#### **6. Export and Format**

- **Output Formats:**
  - Save annotations in standard formats such as COCO JSON, Pascal VOC XML, or YOLO TXT.
  - Roboflow can be used to do this. 
  
- **Export Process:**
  - Ensure all annotated data is correctly exported and backed up.
