from collections import OrderedDict
import urllib2
import bs4
import sys
import json

# To help get you started, here is a function to fetch and parse apage.
# Given url, return soup.


def url_to_soup(url):
    # bgp.he.net filters based on user-agent.
    try:
        req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0' })
        html = urllib2.urlopen(req).read()
        soup = bs4.BeautifulSoup(html, "html.parser")
        return soup
    except urllib2.URLError:
        print('Exception while establishing connection', sys.exc_info()[0])
    except ConnectionError:
        print('Looks like there is a network problem while requesting', sys.exc_info()[0])
    except urllib2.Request.RequestException:
        print('Request Exception',sys.exc_info()[0])
    except urllib2.Request.HTTPError:
        print(' HTTP Error', sys.exc_info()[0])
    except urllib2.Request.TooManyRedirects:
        print('Bad URL',sys.exc_info()[0])
    except urllib2.Request.TimeOut:
        print('Request timed out. It is taking too long for a request response', sys.exc_info()[0])


def scrapping_countries(soup):
    print('Scraping the Countries list in the home page.....')
    country_rows = soup.findAll('tr')
    countries_list = list()
    for each_row in country_rows[1:]:
        try:
            report_href = each_row.find('a')['href'].encode('utf-8')
            # print(report_href)
            countries_list.append(report_href)
        except AttributeError:
            print('No country reports found', sys.exc_info()[0])

    return countries_list


def scraping_ASNs(countries_list):
    print('Scraping the ASN for each country.....')
    # creating a dictionary to hold all ASN's
    ASN_dict = OrderedDict()

    for url in countries_list:

        # Identify the country code from the 'a' tag's attribute 'href' value "/Country/US"
        country_code = url.split('/')[2]
        print('Processing for Country ', country_code)

        # Open the related countries URL
        soup = url_to_soup('https://bgp.he.net' + url)

        # Identifying the table with the ASN contents
        try:
            asn_table = soup.find("table", attrs={'id': 'asns'})
            asns_rows = asn_table.findAll("tr")

        except AttributeError:
            print(sys.exc_info()[0])
            print('No Active ASNs for ', country_code)
            continue

        # Parsing each row in the table excluding the table headers
        for each_row in asns_rows[1:]:
            # Identifying the text in the current row and applying UTF-8 encoding
            td_list1 = each_row.get_text().encode('utf-8')

            # Stripping the extra new line character from the text to avoid any data nuisance
            # and splitting the text to created a list
            td_list = td_list1.strip('\n').split('\n')
            # print(td_list)

            # Removing the 'AS' from each ASN
            ASN_number = int(td_list[0][2:])

            ASN_dict[ASN_number] = {
                                    'Country': country_code,
                                    'Name': td_list[1],
                                    'Routes v4': td_list[3],
                                    'Routes v6': td_list[5]

                                }
            # print( ASN_dict[ASN_number])
    return ASN_dict


def json_dump(ASNs):
    file = open('ASNs.json', 'w')
    json_format = json.dumps(ASNs)
    file.write(json_format)
    file.close()


if __name__ == '__main__':

    home_url = 'https://bgp.he.net/report/world'
    soup = url_to_soup(home_url)

    countries = scrapping_countries(soup)
    # print(countries)
    ASNs = scraping_ASNs(countries)
    # print(ASNs)
    json_dump(ASNs)
    print('Scraping Data. Please check the data in ASNs.json file')

