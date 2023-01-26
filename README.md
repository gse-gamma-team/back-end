# back-end

This is a simple Python Flask server which for the prototype stage only acts as an interface with the AI model.

## Installation

NOTE: The installation guide assumes you are using a virtual environment as that was how this was developed.

1. Clone this project
2. Create a virtual environment
3. Install the required packages by running `pip install -r requirements.txt`
4. Clone the [model](https://github.com/gse-gamma-team/trash-bin-fullness-model) into the `model` directory under `app`

## Usage

### Running the Server

You can run the server like any other Flask project.

```
flask --app app --debug run
```

### Endpoints

#### train_model

The `train_model` endpoint trais a model and saves it. It takes the following parameters.

| Parameter | Description | Default Value |
| --- | --- | --- |
| split | Which day of the week will be used as the test data. | Fri |
| location | Which demo region to be used. | Shiga |
| preprocess | To preprocess or not. | None |
| model | Which model to use. | XG |
| scoring | What scoring method is used. | f1_macro |

#### get_chart

The `get_chart` endpoint visualises the predictions for a single day of the week and returns the image. It takes the following parameters.

| Parameter | Description | Default Value |
| --- | --- | --- |
| path | The name (path) of the image file. Required. | |
| day | Which day to visualise. | Mon |
