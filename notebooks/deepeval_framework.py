import asyncio
import os, time, json
from dotenv import load_dotenv
from google.cloud import aiplatform


from deepeval import evaluate

from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.models.base_model import DeepEvalBaseLLM

from deepeval.benchmarks import MMLU, HellaSwag, HumanEval,TruthfulQA
from deepeval.benchmarks.tasks import HumanEvalTask, HellaSwagTask, MMLUTask, TruthfulQATask
from deepeval.benchmarks.modes import TruthfulQAMode


from deepeval.metrics.ragas import RagasMetric
from deepeval.metrics import (
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric
)

from deepeval.metrics import GEval
from deepeval.metrics import AnswerRelevancyMetric


# For Gooogle VertexAI SDK
# from langchain_google_vertexai import (
#     ChatVertexAI,
#     HarmBlockThreshold,
#     HarmCategory
# )



# safety_settings = {
#     HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
#     HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
#     HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
#     HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
#     HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
# }
from langchain_google_genai import ChatGoogleGenerativeAI



from google.generativeai.types.safety_types import HarmBlockThreshold, HarmCategory

safety_settings = {
HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE, 
HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH, 
HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE, 
HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,

}


load_dotenv()
huggingfaceToken = os.getenv("HuggingFace") #get huggeface token from .env file
os.environ["GOOGLE_API_KEY"]  = os.getenv("GOOGLE_API_KEY") #get google api key from .env file




# default CUstom LLMs for Evaluation
class GoogleVertexAI(DeepEvalBaseLLM):
    """
     class for implement Google VertexAI for DeepEval
    """
    def __init__(self, model):
        self.model = model

    def load_model(self):
        return self.model
    
    def generate(self, prompt : str) -> str:
        chatModel = self.load_model()
        return chatModel.invoke(prompt).content
    
    async def a_generate(self, prompt : str) -> str:
        chatModel = self.load_model()
        ret = await chatModel.ainvoke(prompt)
        return ret.content
    
    def get_model_name(self):
        return "Google Vertex AI"
    

class DeepEvalFramework:
    """
    DeepEvalFramework class for evaluating LLMs
    
    """
    def __init__(self, modelName, task):
        self.modelName = modelName
        self.task = task
        self.llm = ChatGoogleGenerativeAI(model=modelName, 
                                          safety_settings=safety_settings)
        self.model = GoogleVertexAI(self.llm)














if __name__ == '__main__':
    # Define the ground truth and predicted text
    deepEval = DeepEvalFramework("Google Vertex AI", "Chat")
    