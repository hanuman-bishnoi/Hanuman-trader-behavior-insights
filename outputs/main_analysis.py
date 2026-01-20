import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs directory if it doesn't exist
if not os.path.exists('outputs'):
    os.makedirs('outputs')

def run_analysis():
    print("--- Starting Analysis ---")
    
    # 1. Load Datasets
    # Make sure your CSV files are in the 'data' folder
    fg_df = pd.read_csv('data/fear_greed_index.csv')
    hist_df = pd.read_csv('data/historical_data.csv')

    # 2. Process Dates
    print("Processing dates...")
    fg_df['date'] = pd.to_datetime(fg_df['date'])
    hist_df['Timestamp IST'] = pd.to_datetime(hist_df['Timestamp IST'], dayfirst=True)
    
    hist_df['date_only'] = hist_df['Timestamp IST'].dt.date
    fg_df['date_only'] = fg_df['date'].dt.date

    # 3. Merge Data
    merged_df = pd.merge(hist_df, fg_df[['date_only', 'value', 'classification']], 
                         on='date_only', how='left')
    
    # Calculate Win Rate (is_win is True if Closed PnL > 0)
    merged_df['is_win'] = merged_df['Closed PnL'] > 0

    # 4. Generate Summary Statistics
    print("Calculating statistics...")
    stats = merged_df.groupby('classification').agg({
        'Closed PnL': 'mean',
        'Size USD': 'mean',
        'is_win': 'mean',
        'Account': 'count'
    }).rename(columns={'Account': 'Trade_Count', 'is_win': 'Win_Rate'})
    
    # Convert Win Rate to percentage
    stats['Win_Rate'] = stats['Win_Rate'] * 100
    stats = stats.sort_values('Closed PnL', ascending=False)

    print("\n--- Summary Statistics (by Sentiment) ---")
    print(stats)

    # 5. Visualizations
    plt.style.use('ggplot')
    
    # Plot 1: Profitability & Win Rate
    fig, ax1 = plt.subplots(figsize=(12, 6))
    sns.barplot(x=stats.index, y='Closed PnL', data=stats, ax=ax1, palette='viridis')
    ax1.set_title('Avg Profitability & Win Rate by Market Sentiment')
    ax1.set_ylabel('Average Closed PnL ($)')
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('outputs/sentiment_performance.png')
    
    # Plot 2: Correlation
    plt.figure(figsize=(10, 8))
    corr = merged_df[['value', 'Closed PnL', 'Size USD', 'Execution Price', 'is_win']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.savefig('outputs/correlation_heatmap.png')

    print("\nSuccess! Check the 'outputs' folder for charts and 'data/merged_data.csv' for the dataset.")
    merged_df.to_csv('data/merged_data.csv', index=False)

if __name__ == "__main__":
    run_analysis()