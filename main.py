from flask import Flask, render_template,jsonify
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup


@app.route("/", methods= ['GET'])
def result():
	URL = 'https://sfbay.craigslist.org/search/cto?sort=date&searchNearby=2&nearbyArea=63&nearbyArea=187&nearbyArea=43&nearbyArea=373&nearbyArea=709&nearbyArea=189&nearbyArea=454&nearbyArea=285&nearbyArea=96&nearbyArea=102&nearbyArea=188&nearbyArea=92&nearbyArea=12&nearbyArea=191&nearbyArea=62&nearbyArea=710&nearbyArea=708&nearbyArea=97&nearbyArea=707&nearbyArea=208&nearbyArea=346&nearbyArea=456&max_price=15000&min_auto_year=2000&auto_title_status=1%27'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='sortable-results')
	elements = results.find_all('li', class_='result-row')
	dictlist = []

	for elem in elements:

		ref = elem.find('a', class_="result-title hdrlnk")
		price = elem.find('span', class_='result-price')

		dict = {}

		link = elem.find('a').get('href')
		dict['link'] = link
		dict['ref'] = ref.string
		dict['description'] = price.string

		dictlist.append(dict)

	return render_template("feed.html", data=dictlist)

if __name__ == '__main__':
   app.run()