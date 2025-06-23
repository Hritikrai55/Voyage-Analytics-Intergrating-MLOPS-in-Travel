from setuptools import setup, find_packages

setup(
    name='hotel_price_prediction',
    version='0.1.0',
    description='A Streamlit app for hotel price prediction using machine learning',
    author='Hritik Rai',
    author_email='hritikrai55@gmail.com',
    packages=find_packages(),
    install_requires=[
        'streamlit==1.35.0',
        'pandas==2.2.2',
        'scikit-learn==1.4.2',
        'python-dotenv==1.0.1',
        'joblib==1.4.2',
    ],
    include_package_data=True,
    python_requires='>=3.10',
)
