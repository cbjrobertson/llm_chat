import setuptools

setuptools.setup(
     name='psy_llm_chat',  
     version='0.1.2',
     py_modules=['psy_llm_chat'] ,
     author="Cole Robertson",
     author_email="cbjrobertson@gmail.com",
     description="A Package for chatting with LLMs",
     long_description="A Package for chatting with LLMs",
    long_description_content_type="text",
     url="https://github.com/cbjrobertson/llm_chat",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )