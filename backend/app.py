from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from model.mnist_loader import load_model

app = FastAPI()

# Load the trained net2 model at startup
model = load_model()

class DigitInput(BaseModel):
    pixels: list[float]  # List of 784 grayscale pixel values (flattened 28x28)

@app.post("/predict")
async def predict(data: DigitInput):
    try:
        # Convert input to 784x1 vector for feedforward
        input_vector = np.array(data.pixels).reshape((784, 1))
        output = model.feedforward(input_vector)
        prediction = int(np.argmax(output))
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
