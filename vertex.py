"""from vertexai.preview.generative_models import (GenerativeModel,
                                                )

model= GenerativeModel("gemini-pro",generation_config={"temperature":0},
                       )
chat=model.start_chat()

promt="What is the stock price of apple?"
respone=chat.send_message(promt)

print("Chat Response :",respone.text)"""

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

def gen_promt(ver_key,promt_text):
  genai.configure(api_key=ver_key)


  # Set up the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

  convo = model.start_chat(history=[])
  """{
    "role": "user",
    "parts": ["How to do api call for gemini using python?"]
  },
  {
    "role": "model",
    "parts": [
      "## Gemini API Calls with Python: A Basic Guide\n\nGemini offers a REST API for interacting with their exchange programmatically. Here's how to perform API calls using Python:\n\n**1. Dependencies:**\n\n*   **Requests Library:** Install it using `pip install requests`. This library simplifies HTTP requests.\n\n**2. Authentication:**\n\nGemini uses API keys for authentication. You'll need to:\n\n*   **Obtain API Keys:** Generate your API key and secret from the Gemini Account settings. Keep them secure!\n*   **Set Up Authentication:**\n    *   For private API endpoints (requiring authentication), create a payload dictionary with your API key and a \"nonce\" (unique number, often a timestamp).\n    *   Use the `hmac` library to sign the payload with your secret key, creating a signature.\n    *   Include both the signature and API key in the request headers.\n\n**3. Making Requests:**\n\n*   **Import Libraries:**\n\n```python\nimport requests\nimport hmac\nimport hashlib\nimport time\n```\n\n*   **Define API Endpoints:** Gemini provides various endpoints for different functionalities. Refer to the [Gemini API documentation](https://docs.gemini.com/rest-api/) for specifics.\n\n*   **Construct the Request:**\n\n```python\n# Example: Getting your available balances\nurl = \"https://api.gemini.com/v1/balances\"\nnonce = str(int(time.time() * 1000))\npayload = {\"nonce\": nonce}\n\n# Replace with your actual API key and secret\napi_key = \"YOUR_API_KEY\"\napi_secret = \"YOUR_API_SECRET\".encode()\n\nsignature = hmac.new(api_secret, payload.encode(), hashlib.sha384).hexdigest()\n\nheaders = {\n    \"Content-Type\": \"text/plain\",\n    \"X-GEMINI-APIKEY\": api_key,\n    \"X-GEMINI-PAYLOAD\": payload,\n    \"X-GEMINI-SIGNATURE\": signature\n}\n\nresponse = requests.post(url, headers=headers)\n```\n\n*   **Handling Response:**\n\n```python\nif response.status_code == 200:\n    data = response.json()\n    # Process the returned JSON data\nelse:\n    print(f\"Error: {response.status_code}, {response.text}\")\n```\n\n**4. Specific Examples:**\n\n*   **Placing Orders:** Refer to the \"/v1/order/new\" endpoint documentation for parameters like symbol, amount, price, etc.\n*   **Getting Trade History:** Use the \"/v1/mytrades\" endpoint.\n*   **Market Data:** Access public market data without authentication using endpoints like \"/v1/pubticker/btcusd\".\n\n**5. Security Best Practices:**\n\n*   **Never share your API secret.**\n*   **Use secure connections (HTTPS).**\n*   **Consider implementing rate limiting and error handling.**\n\n**Remember:** This is a basic framework. You'll need to adapt it to your specific needs and refer to the Gemini API documentation for detailed endpoint specifications and parameters."]
  },"""

  convo.send_message(promt_text)
  #"can u provide key words to make my projects in my resume match the job description my resume projects PERSONAL PROJECTS Face detection using open CV Developed a face detection application incorporating Sentiment analysis, using openCV and achieved 94% Accuracy Tools and Technologies: Python, OpenCV, AdaBoost Object detection for autonomous driving vehicles Developed a object detection application using openCV and achieved 85% Accuracy Tools and Technologies: Python, OpenCV, Yolo ACADEMIC PROJECTS Gravitational Wave and pulsar detection Developed a application to detect and simulate gravitational wave and pulsar star. Tools and Technologies: Python, Html, css Pharmacy Management System A web-based application to store and access details of medicine, vendors, customers, and employees. This aids us in reducing medicine fraud and also helps us improve pharmacist efficiency. Tools and Technologies: Python,MySQL, Django • Lead a team of 4 members • Planned tasks, schedules and deliverables • Performed Peer Reviews Online Examination Management System The application consists of both an administrator login and a student login. We can add quizzes for various subjects and keep track of each student's results. Personalised administrator login provides teachers a comprehensive view of their students’ performance. Tools and Technologies: ZAMP database Server, SQL, PHP (backend), Python (frontend) • Lead a team of 4 members • Planned tasks, schedules and deliverables • Performed Peer Reviews. Job description is Experience – 4 years and above Industry knowledge - Knows basic principles of industry lexicon, competitor landscape, sub-verticals and related best practices in order to provide suggestions for specific functional processes. Basic understanding of industry standards to document current customer compliance and gaps. Technical Requirements: or higher degree in STEM subject. experience in building and deploying machine learning models. in conceptualize, formulate, prototype and implement algorithms to solve business problems. least 3 years of OOP development using Python, with excellent and broad knowledge of popular Python packages, e.g. statsmodels, sktime, lightgbm etc experience in complete SDLC process. in Agile methodologies and hypothesis-driven approach, good to have. Analytical ability - Looks at data from multiple sources and integrates data/inputs in a manner to build cause effect linkages to arrive at key issues. Uses understanding of the problem to arrive at multiple solution alternatives keeping in mind the various stakeholders and assess the pros and cons of all the alternatives to arrive at the optimal solution Ability to suggest Analytics algorithms to use based on business situation mindful of fundamental assumptions in the algorithms; OR Work with other data scientists as a team to understand algorithms suggested and provide QA in algorithm choice from a business perspective Responsible for successful delivery of Advanced Analytics solutions and services in client consulting environments; experience in optimization (linear, mixed integer, constraint programming), simulation, and/or predictive analytics using AAO tools, such as SAS or SPSS and other Tools R and Python. B usiness acumen - Understands the linkages of metrics and end objectives to key business drivers and aligns team efforts to deliver on it. Demonstrates basic understanding of business financial parameters and is aware of business value impact of activities and decisions taken by him/her and team. High Impact Communication - Assesses the target audience need, prepares and practices a logical flow, answers audience questions appropriately and sticks to timeline. Responsibilities: with existing team to develop, optimize and deploy counterfactual and promotion optimization models. high quality and robust code. in the improvement and scalability enhancement tasks on the code base. and upskill more junior members of the team. Nice to have: with cloud platform, particular Azure and optimization libraries such as Gurobi. in depth understanding of statistical modelling techniques and the mathematical foundations of applied ML algorithms and models. can u enhance my project as per requirement?"
  return convo.last.text
