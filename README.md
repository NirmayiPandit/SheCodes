
# Eduventure

Eduventure is an AI-driven platform designed to provide personalized career guidance to students in educational institutions. Leveraging machine learning algorithms, Eduventure analyzes a wide range of student data to offer tailored recommendations for courses, topics, and career fields based on individual preferences, academic performance, and ongoing trends.

## Key Features

- **Data Collection:** Gathers comprehensive student data including academic records, preferences, interests, goals, and feedback.
- **Machine Learning Models:** Employs algorithms to analyze data and uncover patterns for academic and career insights.
- **Personalized Recommendations:** Provides tailored guidance on courses, topics of focus, and potential career fields.
- **Interactive Interface:** Offers a user-friendly interface for seamless interaction.
- **Continuous Improvement:** Incorporates feedback to enhance recommendation accuracy over time.

## Tech Stack

- **Backend:** Flask, Python
- **Machine Learning Library:**  Pytorch
- **Web Framework:** Flask , HTML5, CSS3, JS, Bootstrap
- **Database Management System:** MySQL (not implemented yet)

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11.x
- pip (Python package installer)
- MySQL (optional)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/NirmayiPandit/SheCodes.git
    cd SheCodes
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the LLM locally:
    - Install the ollama locally with all the required applications.
    - Start the ollama with 'mistral' profile.([tutorial)](https://docs.privategpt.dev/installation/getting-started/installation)

4. Run the application:
    ```sh
    python app.py (for connecting the auth page to form)
    python format_data.py (for connecting the Local LLM to Program via API)
    index.html
    ```

### Usage

- Access the platform at `http://localhost:5000`.
- Sign up and provide your academic and personal information.
- Get personalized course and career recommendations.

## Folder Structure

```plaintext
SheCodes/
├── README.md
├── requirements.txt
├── index.html
├── dashboard.html
├── results.html
├── dashb.html
├── assets/..
├──Login/
│   ├── index.html
│   ├── signup.html
│   ├── others/..
└── question_final/
    └── data/submissions.csv
	└── app.py
	└──format_data.py
	└── llm_responses.txt

```
## Note

->If something is not working or getting connection error try changing the host address and relative path of the resources.
->If you are getting slow output that's totally hardware dependent. (you can use cuda cores for better performance)

## Screenshots
![Homepage](https://github.com/NirmayiPandit/SheCodes/assets/137396151/16af85c2-7e97-4334-ac04-f51b79ab7f04)
![Dashboard](https://github.com/NirmayiPandit/SheCodes/assets/137396151/d3446c59-f319-4f2e-9733-7b1b7568a4fc)
![LLM Response](https://github.com/NirmayiPandit/SheCodes/assets/137396151/2d486da0-ff91-4af4-9106-1b516a815d7e)

## Contributing
We welcome contributions from the cybersecurity community! If you'd like to contribute to the project, please follow our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, suggestions, or want to contribute to this project, please feel free to reach out to the developers:
- [Nirmayi](https://github.com/NirmayiPandit)
- [Prince](https://github.com/hackstyx)
- [Lalitha](https://github.com/lalithaprakash)
- [Sudhanshu](https://github.com/sagewiiz)
