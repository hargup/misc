import requests
from bs4 import BeautifulSoup
import os
from requests.exceptions import ConnectionError

with open('visited_websites.txt', 'r') as f:
    visited_websites = [line.strip() for line in f]

# List to store design websites
design_websites = []

# Create a directory for caching website content
if not os.path.exists('website_cache'):
    os.makedirs('website_cache')

# Iterate over each website
from concurrent.futures import ThreadPoolExecutor

def process_website(website):
    try:
        # Check if the website content is cached
        if os.path.exists(f'website_cache/{website}.txt'):
            with open(f'website_cache/{website}.txt', 'r') as f:
                text_only = f.read()
        else:
            try:
                # Load the website homepage
                response = requests.get(f'http://{website}')
                soup = BeautifulSoup(response.text, 'html.parser')
                text_only = soup.get_text()
            except ConnectionError:
                print(f'Error loading website {website}: Connection Error')
                return None

            # Save the website content for caching
            with open(f'website_cache/{website}.txt', 'w') as f:
                f.write(text_only)

        # Check if the website is a design website
        if 'design' in text_only:
            return website
    except Exception as e:
        print(f'Error loading website {website}: {e}')
        return None

with ThreadPoolExecutor(max_workers=10) as executor:
    design_websites = list(filter(None, executor.map(process_website, visited_websites)))

# Print the list of design websites
print(design_websites)

# Print the number of visited websites
print(f'Visited {len(visited_websites)} websites.')



# Error loading website %5b::1%5D:5002: Failed to parse: http://%5b::1%5D:5002
# Error loading website -mt.co: Connection Error
# Error loading website (svilentodorov.xyz: Connection Error
# Error loading website 0.0.0.0:8935: Connection Error
# Error loading website -db.deis.unibo.it: Connection Error
# Error loading website 0.0.0.0:6274: Connection Error
# Error loading website 127.0.0.1:54991: Connection Error
# Error loading website 0.0.0.0:8000: Connection Error
# Error loading website 127.0.0.1:7860: Connection Error
# Error loading website 127.0.0.1:8080: Connection Error
# Error loading website 127.0.0.1:49226: Connection Error
# Error loading website 192.168.0.228:8080: Connection Error
# Error loading website 2.gosection8.com: Connection Error
# Error loading website 25.subprocess.run: Connection Error
# Error loading website 2.affinity.net: Connection Error
# Error loading website 2.imm.dtu.dk: Connection Error
# Error loading website 8.tax.ny.gov: Connection Error
# Error loading website accountantslawlab.com: Connection Error
# Error loading website 1redird.com: Connection Error
# Error loading website 2022looped.com: Connection Error
# Error loading website 3docs.com: Connection Error
# Error loading website 100vanness.com: Connection Error
# /Users/harshwork/opt/anaconda3/lib/python3.10/site-packages/bs4/builder/__init__.py:545: XMLParsedAsHTMLWarning: It looks like you're parsing an XML document using an HTML parser. If this really is an HTML document (maybe it's XHTML?), you can ignore or filter this warning. If it's XML, you should know that using an XML parser will be more reliable. To parse this document as XML, make sure you have the lxml package installed, and pass the keyword argument `features="xml"` into the BeautifulSoup constructor.
#   warnings.warn(
# Error loading website ai.orbofi.com: Connection Error
# Error loading website airchina.com.cn: Connection Error
# Error loading website aitbutwhy.com: Connection Error
# Error loading website akingup.com: Connection Error
# Error loading website aishbhardwaj.com: Connection Error
# Error loading website alnut.io: Connection Error
# Error loading website almart.com: Connection Error
# Error loading website andb.ai: Connection Error
# Error loading website andrew.today: Connection Error
# Error loading website animeai.lol: Connection Error
# Error loading website answerchatai.com: Connection Error
# Error loading website antipope.org: Connection Error
# Error loading website anyplacehere.me: Connection Error
# /Users/harshwork/code/misc/designer_list_finder/find_design_websites.py:29: MarkupResemblesLocatorWarning: The input looks more like a filename than markup. You may want to open this file and pass the filehandle into Beautiful Soup.
#   soup = BeautifulSoup(response.text, 'html.parser')
# Error loading website api.clerk.dev: Connection Error
# Error loading website api.countapi.xyz: Connection Error
# Error loading website api.spotnana.com: Connection Error
# Error loading website 150.136.94.200:7860: Connection Error
# Error loading website 172.18.0.2:8080: Connection Error
# Error loading website aetnacvshealth.com: Connection Error
# Error loading website app.qbo.intuit.com: Connection Error
# Error loading website app.tipsytom.com: Connection Error
# Error loading website apps.posthog.com: Connection Error
# Error loading website apps.ups.com: Connection Error
# Error loading website argovisa.com: Connection Error
# Error loading website arhouse.la: Connection Error
# Error loading website armest.ai: Connection Error
# Error loading website arp.dev: Connection Error
# Error loading website arpcast.com: Connection Error
# Error loading website archive.is: Connection Error
# Error loading website archive.ph: Connection Error
# Error loading website archive.today: Connection Error
# Error loading website atermelontools.com: Connection Error
# Error loading website auth.console.anthropic.com: Connection Error
# Error loading website api.juspay.in: Connection Error
# Error loading website avabear.xyz: Connection Error
# Error loading website api.search.brave.com: Connection Error
# Error loading website aves.digitalocean.com: Connection Error
# Error loading website ashingtonpost.com: Connection Error
# Error loading website beta.lightapi.com: Connection Error
# Error loading website bhari.com: Connection Error
# Error loading website bikebazaar.com: Connection Error
# Error loading website blenderbot.ai: Connection Error
# Error loading website blog.trailmeme.com: Connection Error
# Error loading website blog.steamship.com: Connection Error
# Error loading website bls.gov: Connection Error
# Error loading website brancher.ai: Connection Error
# Error loading website brightmirror.co: Connection Error
# Error loading website api.checkout.com: Connection Error
# Error loading website businesssearch.sos.ca.gov: Connection Error
# Error loading website api.travelbank.com: Connection Error
# Error loading website bwiairport.com: Connection Error
# Error loading website c.xkcd.com: Connection Error
# Error loading website calcalistech.com: Connection Error
# Error loading website bestaiprompts.art: Connection Error
# Error loading website captionbot.ai: Connection Error
# Error loading website capture.onboard.oryxcomms.com: Connection Error
# Error loading website catwalkai.com: Connection Error
# Error loading website cdc.iitkgp.ernet.in: Connection Error
# Error loading website ceac.state.gov: Connection Error
# Error loading website cgisaopaulo.gov.in: Connection Error
# Error loading website chat.langchain.dev: Connection Error
# Error loading website chatoeg.ai: Connection Error
# Error loading website checkcoverage.apple.com: Connection Error
# Error loading website chrisstrobl.com: Connection Error
# Error loading website bvp.com: Connection Error
# Error loading website ca-dmv-vo.prod.simpligov.com: Connection Error
# Error loading website community.booking.com: Connection Error
# Error loading website cs.virginia.edu: Connection Error
# Error loading website curiousdk.com: Connection Error
# Error loading website checkoutshopper-live-us.adyen.com: Connection Error
# Error loading website cuvetter.tech: Connection Error
# Error loading website d.agkn.com: Connection Error
# Error loading website daqfgzygtdrlbvjjwyd.supabase.co: Connection Error
# Error loading website davebking.com: Exceeded 30 redirects.
# Error loading website dcmventures.com: Connection Error
# Error loading website consent.yahoo.com: Connection Error
# Error loading website descript.ai: Connection Error
# Error loading website defenderservices.com: Connection Error
# Error loading website devtools.ai: Connection Error
# Error loading website dialdairy.app: Connection Error
# Error loading website dictionary.cambridge.org: Connection Error
# Error loading website diningandcooking.com: Connection Error
# Error loading website drda.templatesearch.org: Connection Error
# Error loading website dreamer.page: Connection Error
# Error loading website corbu.ai: Connection Error
# Error loading website digitalinvoice.jio.com: Connection Error
# Error loading website e-jugaad.com: Connection Error
# Error loading website eallwantsomeone.org: Connection Error
# Error loading website earlyflower.click: Connection Error
# Error loading website eaviate.io: Connection Error
# Error loading website eb.cs.ucdavis.edu: Connection Error
# Error loading website eb.dev: Connection Error
# Error loading website eb.miniextensions.com: Connection Error
# Error loading website eb.eecs.utk.edu: Connection Error
# Error loading website eb.senpex.com: Connection Error
# Error loading website ebapp.ftb.ca.gov: Connection Error
# Error loading website eb.whatsapp.com: Connection Error
# Error loading website ebchat.freenode.net: Connection Error
# Error loading website ebdev.polymath.chat: Connection Error
# Error loading website ebhook.site: Connection Error
# Error loading website ebpayments.billmatrix.com: Connection Error
# Error loading website ebscrapingapi.com: Connection Error
# Error loading website ebsiteclosers.com: Connection Error
# Error loading website ebtoons.com: Connection Error
# Error loading website ellknown.ai: Connection Error
# Error loading website elkes.com: Connection Error
# Error loading website emjcd.com: Connection Error
# Error loading website ericbutton.co: Connection Error
# Error loading website estbridgecap.com: Connection Error
# Error loading website estonwagner.com: Connection Error
# Error loading website evanmiller.org: Connection Error
# Error loading website evisa.mofa.go.jp: Connection Error
# Error loading website ec2-18-237-238-224.us-west-2.compute.amazonaws.com: Connection Error
# Error loading website exploro.plus: Connection Error
# Error loading website evisa.xuatnhapcanh.gov.vn: Connection Error
# Error loading website felvin.xyz: Connection Error
# Error loading website financialregnews.com%20pay%20day%20lending: Connection Error
# Error loading website fdle.state.fl.us: Connection Error
# Error loading website fitgirlssociety.com: Connection Error
# Error loading website flychain.us: Connection Error
# Error loading website flyfrontier.com: Connection Error
# Error loading website forbesindia.com: Connection Error
# Error loading website fortytwoai.com: Connection Error
# Error loading website gen.lib.rus.ec: Connection Error
# Error loading website getshifu.com: Connection Error
# Error loading website getsphere.com: Connection Error
# Error loading website gfycat.com: Connection Error
# Error loading website gigs.bensbites.co: Connection Error
# Error loading website glif.com: Connection Error
# Error loading website glorobinson.co: Connection Error