# Analysis-of-box-office-data-for-the-500-most-relevant-films.
This project analyzes the top 500 most relevant movies based on worldwide box office data.


📌 Description
This project analyzes the top 500 most relevant movies based on worldwide box office data.
What it does:

Cleans and preprocesses data for reliable analysis
Calculates correlations between numerical variables such as production cost and revenue
Identifies and visualizes the highest-budget and highest-grossing movies
Compares worldwide and domestic revenue, highlighting the impact of each market
Calculates percentage contributions of the most profitable movies
Analyzes the evolution of worldwide box office over the last 25 years
Compares revenue by genre (Action, Adventure, and others)
Generates charts and visualizations for better data interpretation

Why it was created:
To understand patterns of success and investment in the film industry
To provide insights into which movies and genres yield the highest return
To enable comparative analysis between worldwide and domestic revenue

Built with:
Programming language: Python
Libraries: Pandas and NumPy for data manipulation and analysis
Library: Matplotlib for data visualization

⚙️ Prerequisites
Before running the project, make sure you have installed:
Python 3.8+
pip

📥 Installation

Clone this repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

pip install pandas numpy matplotlib
▶️ Usage

Place the file top-500-movies.csv in the project folder.

Run the main script:
python analise_filmes.py

The script will:
Display statistics and revenue averages
Show correlation charts, box office distributions, and time evolution
Compare revenues across genres and movies

📊 Example Outputs

Correlation matrix between production cost, worldwide revenue, and domestic revenue
Bar charts of the most expensive and highest-grossing movies
Line chart showing box office trends over the last 25 years
Pie chart showing the Top 20 revenue share
Genre comparison highlighting Action and Adventure movie revenues

📚 Technologies

Pandas → data manipulation and cleaning
NumPy → mathematical operations
Matplotlib → charts and visualizations


📄 License
This project is licensed under the MIT License – see the LICENSE
 file for details.
