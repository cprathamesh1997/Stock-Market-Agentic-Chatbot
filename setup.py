from setuptools import find_packages,setup

setup(name="agentic-trading-system",
       version="0.0.1",
       author="pratham",
       author_email="cprathamesh1997@gmail.com",
       packages=find_packages(),
       install_requires=['lancedb','langchain','langgraph','tavily-python','polygon']
       )