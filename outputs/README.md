Trader Behavior vs. Market Sentiment Analysis
📊 Project Overview
This project investigates the relationship between Bitcoin market sentiment (Fear & Greed Index) and real-world trader performance using historical data from the Hyperliquid platform. By analyzing over 211,000 trade executions, the study identifies how psychological extremes in the market correlate with profitability, capital deployment, and risk management.

📁 Project Structure
The repository is organized to ensure reproducibility and clear data provenance:

data/: Contains the raw input files (historical_data.csv, fear_greed_index.csv) and the final merged_data.csv.

outputs/: Stores the generated visual insights, including PnL distributions and correlation heatmaps.

main_analysis.py: The primary Python script for data cleaning, time-series synchronization, and statistical aggregation.

pdf.py: A specialized reporting script used to generate the final analytical document.

Hanuman_Extended_Report.pdf: The comprehensive final report containing findings and strategic recommendations.

🛠️ Installation & Usage
To replicate the analysis or generate the report, ensure the following Python environment is configured:

Install Dependencies:

Bash

pip install pandas matplotlib seaborn fpdf
Execute Analysis:

Bash

python main_analysis.py
Generate Report:

Bash

python outputs/pdf.py
🧠 Key Insights from the Dataset
The Contrarian Whale (Fear Phase): Average trade sizes reached a maximum of $7,816 during "Fear" periods, indicating that high-volume traders in this dataset aggressively enter positions during market drawdowns.

The Profitability Paradox (Greed Phase): While trade volume decreases during "Extreme Greed," the average PnL peaks at $67.89, demonstrating high efficiency in trend-following momentum strategies.

The Neutral Market Trap: Traders performed worst when sentiment was "Neutral," with average PnL dropping to $34.30, likely due to the lack of clear directional conviction.

🧪 Methodology
Data Synchronization: Standardized IST timestamps to daily dates to enable a precise left-join between execution-level data and daily sentiment scores.

Performance Metrics: Calculated mean Closed PnL, capital deployment (Size USD), and win rates across five distinct sentiment regimes.

Visualization: Utilized Seaborn heatmaps and Matplotlib bar charts to identify non-linear relationships between sentiment and execution quality.

🚀 Future Roadmap
Predictive Modeling: Integrating an XGBoost classifier to predict trade success probability based on real-time sentiment signals.

Funding Rate Analysis: Correlating carry-costs with sentiment extremes to evaluate the impact of market leverage on net profitability.