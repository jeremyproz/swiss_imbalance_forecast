# from imbalance_forecast.data.load import load_data
# from imbalance_forecast.models.chronos2 import forecast
from imbalance_forecast.utils.config import load_config


def main():
    config = load_config("configs/chronos2.yaml")

    # data = load_data(config)
    # predictions = forecast(data, config)


if __name__ == "__main__":
    main()