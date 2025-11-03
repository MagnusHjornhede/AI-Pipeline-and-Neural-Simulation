import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def load_data(filepath: str) -> pd.DataFrame:

    feature_names = [f"feature_{i}" for i in range(1, 243)]  # 242 feature columns
    data = pd.read_csv(filepath, header=None, names=feature_names)
    data.rename(columns={
        data.columns[-2]: 'gesture name',
        data.columns[-1]: 'gesture ID'
    }, inplace=True)
    return data


def check_missing_values(_input: pd.DataFrame):
    missing_values = _input.isnull().sum()
    columns_with_missing_values = missing_values[missing_values > 0]
    print("Missing values")
    print(columns_with_missing_values)


def print_heatmap(_input: pd.DataFrame, _name: str):
    plt.figure(figsize=(12, 5))
    sns.heatmap(_input.isnull(), cmap='viridis', cbar=True, yticklabels=False)
    plt.title(_name)
    plt.show()


def plot_boxplot(_input: pd.DataFrame, _name: str):
    _input.boxplot(figsize=(12, 8))
    plt.xticks(rotation=90)  # Rotate x labels
    plt.title(_name)
    plt.show()


if __name__ == '__main__':
    # Load data
    train_data = load_data('datasets/train-final.csv')
    test_data = load_data('datasets/test-final.csv')

    # convert into dataFrame
    train_data = pd.DataFrame(train_data)
    test_data = pd.DataFrame(test_data)

    # Check for missing values
    print("Checking train_data")
    check_missing_values(train_data)
    print_heatmap(train_data, "Missing data points in train-final.csv")
    print("Check test_data")
    check_missing_values(test_data)
    print_heatmap(test_data, "Missing data points in test-final.csv")

    # Assign data for training
    X = train_data.drop(columns=['gesture name', 'gesture ID'])
    y = train_data['gesture ID']  # gesture ID as the target label
    X.fillna(X.mean(), inplace=True)
    # X.dropna(inplace=True)

    # Assign data for testing
    test_data.dropna(inplace=True)  # Just drop rows missing testdata
    X_test = test_data.drop(columns=['gesture name', 'gesture ID'])
    y_test = test_data['gesture ID']  # gesture ID as  target label
    X_test.fillna(X.mean(), inplace=True)

    positions_data = X.iloc[:, :60]  # first 60 columns
    cosine_angles_data = X.iloc[:, 60:120]  # next 60 columns
    mean_positions_data = X.iloc[:, 120:180]  # next 60 columns
    std_positions_data = X.iloc[:, 180:240]  # next 60 columns

    # Print out a plot
    #plot_boxplot(positions_data, 'positions data')
    #plot_boxplot(cosine_angles_data, 'cosine angles data')
    #plot_boxplot(mean_positions_data, 'mean positions data')
    #plot_boxplot(std_positions_data, 'std positions data')

    # Standardlization
    first_60_features = train_data.iloc[:, :60]
    scaler = MinMaxScaler()
    normalized_first_60_features = scaler.fit_transform(first_60_features)
    #scaler = StandardScaler()
    #normalized_first_60_features = scaler.fit_transform(first_60_features)
    train_data.iloc[:, :60] = normalized_first_60_features

    plot_boxplot(train_data, "First 60 standardization")
