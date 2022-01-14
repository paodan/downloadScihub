#!/usr/bin/python3
import requests
import re
import sys

print(sys.argv)
print(len(sys.argv))
if len(sys.argv) >= 3:
  url = sys.argv[1]
  papers = sys.argv[2::]
# Necessary variable settings
'''
url = 'https://sci-hub.se/'

papers = [
        "Concise Review: MSC-Derived Exosomes for Cell-Free Therapy.",
        "MSC exosome works through a protein-based mechanism of action",
        "Mammalian MSC from selected species: Features and applications",
        "Error paper name"
    ]
'''

headers = {
    'referer': 'https://sci-hub.se/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}


# function definition
def get_html(url, papers = None, headers = None):
    if not url:
        raise Exception("url is None, please check...")
    if isinstance(papers, list):
        data = [{'sci-hub-plugin-check': '', 'request':p} for p in papers]
        res = [requests.post(url, data = d, headers = headers) for d in data]
        res_text = [r.text for r in res]
        return res_text
    else:
        data = {'sci-hub-plugin-check': '', 'request':papers}
        res = requests.post(url, data = data, headers=headers)
        return res.text

def get_pdf_path(html, pattern = "location.href='(.*\\.pdf)"):
    pat = re.compile(pattern)
    if isinstance(html, list):
        pdf_path = [pat.findall(h) for h in html]
    else:
        pdf_path = pat.findall(html)
    return pdf_path

def get_pdf(path):
    res = []
    if isinstance(path, list):
        for p in path:
            try:
                pdf = requests.get(p.replace("\\/", "/")).content
            except Exception:
                pdf = None
            res.append(pdf)
    else:
        res.append(requests.get(path).content)
    return res


def main(url, papers = None, headers = None, pattern = "location.href='(.*\\.pdf)"):
    print(f"===== Get html =====")
    html = get_html(url, papers, headers)
    print(f"===== Get pdf path =====")
    pdf = get_pdf_path(html, pattern = pattern)
    pdf_path = [p[0] if len(p) > 0 else None for p in pdf]
    print(f"===== Get pdf content =====")
    pdf_content = get_pdf(pdf_path)
    if not isinstance(papers, list):
        papers = [papers]
    with open("log.txt", "w") as f_log:
        for idx,p in enumerate(pdf_content):
            print(f"{idx+1}: {papers[idx]} \n   downloading...")
            if p == None:
                print(f"   failed and log into log_file...")
                f_log.write(f"{papers[idx]}\n")
            else:
                print(f"   success")
                pdf_name = re.sub('[\/:?*"<>|]*', '', papers[idx])
                pdf_name = f"{pdf_name}.pdf"
                with open(pdf_name, "wb") as f_pdf:
                    f_pdf.write(p)

# compatible with package
if __name__ == "__main__":
    main(url, papers = papers, headers = headers)

