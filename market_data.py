MARKET_DATA = {
	"Industrial Automation": {
		"salary_range": "$110k - $170k",
		"demand": "High",
		"growth": "Strong",
		"certifications": [
    "AZ-900",
    "AWS Cloud Practitioner",
    "Google Data Analytics"
		]
	},
	"Construction Technology": {
    "salary_range": "$95k - $145k",
    "demand": "Moderate",
    "growth": "Growing",
    "certifications": [
        "PMP",
        "OSHA 30",
        "Autodesk Construction Cloud"
    ]
    }
}


def get_market_data(sector):
	return MARKET_DATA.get(
    sector,
    {
        "salary_range": "Unknown",
        "demand": "Unknown",
        "growth": "Unknown",
        "certifications": []
    }
)
