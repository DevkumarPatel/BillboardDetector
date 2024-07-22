import os
from typing import Literal, Optional
from roboflow import Roboflow
from dotenv import load_dotenv
from roboflow.core.dataset import Dataset

# load the environment
load_dotenv()

def get_roboflow_dataset(
    model_format: Literal["yolov5", "yolov7", "yolov8", "yolov8-obb" , "yolov9"] = "yolov5",
    overwrite: bool = False
) -> Dataset:
    """Gets the roboflow dataset.

    Args:
        model_format (Literal["yolov5", "yolov7", "yolov8", "yolov8-obb" , "yolov9"]): The model format. Defaults to "yolov5".
        overwrite (bool): Whether to overwrite existing files. Defaults to False.

    Returns:
        Dataset: The roboflow dataset object.

    Raises:
        ValueError: If the ROBOFLOW_API_KEY environment variable is not set.
    """
    roboflow_api_key = os.getenv("ROBOFLOW_API_KEY")
    if not roboflow_api_key:
        raise ValueError("ROBOFLOW_API_KEY environment variable is not set")

    rf = Roboflow(api_key=roboflow_api_key)

    project = rf.workspace("advision").project("ooh-detection")
    version = project.version(9)

    # Download or get the data from a saved spot.
    dataset = version.download(
        model_format=model_format,
        location="datasets/ooh-detection",
        overwrite=overwrite
    )

    return dataset

