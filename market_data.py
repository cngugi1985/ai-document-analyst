MARKET_DATA = {
	"Industrial Automation": {
		"salary_range": "$110k - $170k",
		"demand": "High",
		"growth": "Strong"
	}
}


def get_market_data(sector):
	return MARKET_DATA.get(
		sector,
		{
			"salary_range": "Unknown",
			"demand": "Unknown",
			"growth": "Unknown"
		}
	)
