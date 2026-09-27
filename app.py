import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    client = Groq(api_key=api_key)
else:
    client = None


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AdaptiveAI Tutor",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🎓 AdaptiveAI Tutor")
st.subheader("Personalised AI Learning Agent")

st.write(
    "An AI tutor that adapts learning content, difficulty "
    "and explanations based on your performance."
)

st.divider()


# -----------------------------
# Student Profile
# -----------------------------

st.header("👤 Student Profile")

name = st.text_input(
    "Your Name"
)

level = st.selectbox(
    "Current AI Knowledge",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

goal = st.selectbox(
    "What do you want to learn?",
    [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Generative AI"
    ]
)


# -----------------------------
# Start Assessment
# -----------------------------

if st.button("🚀 Start Assessment"):

    if not name:

        st.warning(
            "Please enter your name."
        )

    else:

        st.session_state["name"] = name
        st.session_state["level"] = level
        st.session_state["goal"] = goal
        st.session_state["assessment_started"] = True

        st.success(
            f"Welcome {name}! Let's understand your current knowledge."
        )


# -----------------------------
# Assessment
# -----------------------------

if st.session_state.get(
    "assessment_started",
    False
):

    st.divider()

    st.header("🧠 Initial AI Assessment")

    q1 = st.radio(
        "1. Which programming language is commonly used for AI and Machine Learning?",
        [
            "Python",
            "HTML",
            "CSS",
            "Bootstrap"
        ],
        key="q1"
    )

    q2 = st.radio(
        "2. What does ML stand for?",
        [
            "Machine Learning",
            "Manual Logic",
            "Model Language",
            "Machine Logic"
        ],
        key="q2"
    )

    q3 = st.radio(
        "3. Which of the following is a Machine Learning algorithm?",
        [
            "Linear Regression",
            "HTML",
            "CSS",
            "Bootstrap"
        ],
        key="q3"
    )

    q4 = st.radio(
        "4. Which library is widely used for Machine Learning in Python?",
        [
            "Scikit-learn",
            "React",
            "Bootstrap",
            "Django"
        ],
        key="q4"
    )

    q5 = st.radio(
        "5. What is the purpose of a training dataset?",
        [
            "To train a machine learning model",
            "To design a website",
            "To create CSS styles",
            "To store passwords"
        ],
        key="q5"
    )

    if st.button("📊 Analyse My Skills"):

        score = 0

        if q1 == "Python":
            score += 1

        if q2 == "Machine Learning":
            score += 1

        if q3 == "Linear Regression":
            score += 1

        if q4 == "Scikit-learn":
            score += 1

        if q5 == "To train a machine learning model":
            score += 1

        percentage = int(
            (score / 5) * 100
        )

        st.session_state["score"] = score
        st.session_state["percentage"] = percentage
        st.session_state["assessment_completed"] = True


# -----------------------------
# Assessment Result
# -----------------------------

if st.session_state.get(
    "assessment_completed",
    False
):

    score = st.session_state["score"]
    percentage = st.session_state["percentage"]

    st.divider()

    st.header("📈 Your Assessment Result")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Score",
            f"{score}/5"
        )

    with col2:

        st.metric(
            "Percentage",
            f"{percentage}%"
        )

    with col3:

        if percentage < 50:

            detected_level = "Beginner"

        elif percentage < 80:

            detected_level = "Intermediate"

        else:

            detected_level = "Advanced"

        st.metric(
            "Detected Level",
            detected_level
        )


    # -----------------------------
    # Level Analysis
    # -----------------------------

    if percentage < 50:

        st.warning(
            "Your foundation needs improvement."
        )

        st.write(
            "We recommend starting with AI fundamentals "
            "and basic Machine Learning concepts."
        )

    elif percentage < 80:

        st.info(
            "You have a basic foundation."
        )

        st.write(
            "We recommend strengthening Machine Learning "
            "concepts through practical exercises."
        )

    else:

        st.success(
            "You have a strong foundation!"
        )

        st.write(
            "You can move towards advanced AI and "
            "Generative AI concepts."
        )


    # -----------------------------
    # Personalised Roadmap
    # -----------------------------

    st.divider()

    st.header("🗺️ Personalised Learning Roadmap")

    if percentage < 50:

        roadmap = [
            "AI Fundamentals",
            "Python for AI",
            "Introduction to Machine Learning",
            "Basic ML Algorithms",
            "Simple AI Project"
        ]

    elif percentage < 80:

        roadmap = [
            "Python for AI",
            "Machine Learning Algorithms",
            "Model Evaluation",
            "Feature Engineering",
            "Practical ML Project"
        ]

    else:

        roadmap = [
            "Advanced Machine Learning",
            "Deep Learning",
            "NLP",
            "Generative AI",
            "AI Agent Development"
        ]

    for i, roadmap_topic in enumerate(
        roadmap,
        start=1
    ):

        st.write(
            f"**{i}. {roadmap_topic}**"
        )

    st.success(
        "Your learning path is personalised according to your assessment performance."
    )


# -----------------------------
# AI Tutor
# -----------------------------

st.divider()

st.header("🤖 AI Tutor")

st.write(
    "Ask your tutor anything about AI, Machine Learning or your learning goal."
)

topic = st.text_input(
    "📚 Topic",
    placeholder="Example: Machine Learning"
)

question = st.text_area(
    "💬 Ask your question",
    placeholder="Example: Explain overfitting in simple terms."
)


if st.button("💡 Ask AI Tutor"):

    if not question:

        st.warning(
            "Please enter a question."
        )

    elif not client:

        st.error(
            "Groq API key not found. Please check your .env file."
        )

    else:

        student_level = st.session_state.get(
            "level",
            "Beginner"
        )

        learning_goal = st.session_state.get(
            "goal",
            "Artificial Intelligence"
        )

        prompt = f"""
You are AdaptiveAI Tutor, a personalised AI learning assistant.

Student name:
{st.session_state.get("name", "Student")}

Student current level:
{student_level}

Learning goal:
{learning_goal}

Topic:
{topic}

Student question:
{question}

Instructions:

1. Explain according to the student's level.
2. Use simple language.
3. Give a practical real-world example.
4. Avoid unnecessary complex terminology.
5. Give one short practice question at the end.
6. Encourage the student to continue learning.
"""

        try:

            with st.spinner(
                "🤖 AI Tutor is thinking..."
            ):

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7
                )

            answer = response.choices[0].message.content

            st.subheader(
                "📖 Tutor Explanation"
            )

            st.write(answer)

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )


# -----------------------------
# Adaptive Quiz
# -----------------------------

st.divider()

st.header("🧩 Adaptive Quiz")

st.write(
    "Test your understanding and get a difficulty recommendation based on your performance."
)


quiz_level = st.session_state.get(
    "level",
    "Beginner"
)


# -----------------------------
# Beginner Quiz
# -----------------------------

if quiz_level == "Beginner":

    quiz_questions = [

        {
            "question":
            "Which language is widely used for AI and Machine Learning?",

            "options":
            [
                "Python",
                "HTML",
                "CSS",
                "JavaScript"
            ],

            "answer":
            "Python"
        },

        {
            "question":
            "What does AI stand for?",

            "options":
            [
                "Artificial Intelligence",
                "Automated Internet",
                "Advanced Information",
                "Artificial Internet"
            ],

            "answer":
            "Artificial Intelligence"
        },

        {
            "question":
            "What is Machine Learning?",

            "options":
            [
                "A method where computers learn patterns from data",
                "A web design technique",
                "A database system",
                "A programming language"
            ],

            "answer":
            "A method where computers learn patterns from data"
        }

    ]


# -----------------------------
# Intermediate Quiz
# -----------------------------

elif quiz_level == "Intermediate":

    quiz_questions = [

        {
            "question":
            "Which algorithm is commonly used for classification?",

            "options":
            [
                "Logistic Regression",
                "HTML",
                "CSS",
                "SQL"
            ],

            "answer":
            "Logistic Regression"
        },

        {
            "question":
            "What is overfitting?",

            "options":
            [
                "Model performs well on training data but poorly on unseen data",
                "Model has no data",
                "Model trains too slowly",
                "Model has too few features"
            ],

            "answer":
            "Model performs well on training data but poorly on unseen data"
        },

        {
            "question":
            "Which technique helps reduce overfitting?",

            "options":
            [
                "Regularization",
                "Removing all data",
                "Increasing errors",
                "Deleting the model"
            ],

            "answer":
            "Regularization"
        }

    ]


# -----------------------------
# Advanced Quiz
# -----------------------------

else:

    quiz_questions = [

        {
            "question":
            "Which technique is commonly used to prevent neural network overfitting?",

            "options":
            [
                "Dropout",
                "HTML",
                "Sorting",
                "Normalization only"
            ],

            "answer":
            "Dropout"
        },

        {
            "question":
            "What is the purpose of an attention mechanism in modern NLP models?",

            "options":
            [
                "To focus on relevant parts of the input",
                "To remove all input data",
                "To replace the dataset",
                "To reduce the vocabulary to zero"
            ],

            "answer":
            "To focus on relevant parts of the input"
        },

        {
            "question":
            "What does a validation dataset help with?",

            "options":
            [
                "Evaluating model performance during development",
                "Writing HTML",
                "Creating passwords",
                "Installing Python"
            ],

            "answer":
            "Evaluating model performance during development"
        }

    ]


# -----------------------------
# Display Quiz
# -----------------------------

quiz_answers = []

for i, quiz_question in enumerate(
    quiz_questions
):

    answer = st.radio(
        f"{i + 1}. {quiz_question['question']}",
        quiz_question["options"],
        key=f"adaptive_quiz_{quiz_level}_{i}"
    )

    quiz_answers.append(answer)


# -----------------------------
# Evaluate Quiz
# -----------------------------

if st.button("📊 Evaluate Quiz"):

    quiz_score = 0

    for i, quiz_question in enumerate(
        quiz_questions
    ):

        if quiz_answers[i] == quiz_question["answer"]:

            quiz_score += 1

    quiz_percentage = int(
        (quiz_score / len(quiz_questions)) * 100
    )

    st.session_state["quiz_score"] = quiz_score

    st.session_state["quiz_percentage"] = quiz_percentage


    st.subheader(
        "📈 Quiz Performance"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Quiz Score",
            f"{quiz_score}/{len(quiz_questions)}"
        )

    with col2:

        st.metric(
            "Performance",
            f"{quiz_percentage}%"
        )


    # -----------------------------
    # Adaptive Recommendation
    # -----------------------------

    if quiz_percentage < 50:

        st.warning(
            "Your performance is below 50%."
        )

        st.write(
            "🔄 Adaptive recommendation: "
            "The tutor will provide simpler explanations "
            "and more beginner-level practice."
        )

    elif quiz_percentage < 80:

        st.info(
            "You have a developing understanding."
        )

        st.write(
            "🔄 Adaptive recommendation: "
            "Continue with your current level and practise more."
        )

    else:

        st.success(
            "Excellent performance!"
        )

        st.write(
            "🚀 Adaptive recommendation: "
            "You are ready for more advanced concepts."
        )


# -----------------------------
# Progress Dashboard
# -----------------------------

st.divider()

st.header("📊 Learning Progress")

if st.session_state.get("assessment_completed", False):

    percentage = st.session_state["percentage"]

    st.progress(
        percentage / 100
    )

    st.write(
        f"Current assessment progress: **{percentage}%**"
    )

    if percentage < 50:

        st.write(
            "🎯 Focus on fundamentals and beginner-level practice."
        )

    elif percentage < 80:

        st.write(
            "🎯 Continue practising intermediate AI concepts."
        )

    else:

        st.write(
            "🎯 You are ready for advanced AI topics."
        )

else:

    st.info(
        "Complete the initial assessment to see your learning progress."
    )


# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "🎓 AdaptiveAI Tutor | Personalised Learning powered by AI"
)