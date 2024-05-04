import pandas as pd
import re
import scrape
from random import randint
from time import sleep


class AEA:
    def get_issue(self, journal: str):
        """journal (journal long):
            - app (American Economic Journal: Applied Economics)
            - aer (American Economic Review)
            - jel (Journal of Economic Literature)
            - jep (Journal of Economic Perspectives)
            - mac (American Economic Journal: Macroeconomics)
            - pol (American Economic Journal: Economic Policy)
        """

        url = f"https://www.aeaweb.org/journals/{journal}/issues"
        html = scrape.get_html(url=url)
        issue = html.find_all("article")
        issue = [x.find_all("a") for x in issue]
        issues = []
        for i in issue:
            for j in i:
                j = f"https://www.aeaweb.org{j['href']}"
                issues.append(j)

        return issues
    

    def get_article(self, issue: str):
        try:
            html = scrape.get_html(url=issue)
            article = html.find("section", {"class": "journal-article-group"})
            article = article.find_all("article")
            articles = []

            for i in article:
                try:
                    i = i.find("a")["href"]
                    i = f"https://www.aeaweb.org{i}"
                    articles.append(i)
                except TypeError:
                    pass
            
            return articles
        
        except AttributeError:
            pass
    

    def get_jel(self, article: str, journal_long: str):
        """journal (journal long):
            - app (American Economic Journal: Applied Economics)
            - aer (American Economic Review)
            - jel (Journal of Economic Literature)
            - jep (Journal of Economic Perspectives)
            - mac (American Economic Journal: Macroeconomics)
            - pol (American Economic Journal: Economic Policy)
        """
        
        html = scrape.get_html(url=article)

        try:
            jel = html.find("ul", {"class": "jel-codes"})
            jel = [x.find("strong").text for x in jel.find_all("li")]
            year = html.select("div.journal:nth-child(2)")[0].text
            year = re.sub("[\n\t]", "", year).split(", ")[-1].split(" ")[-1]
            df = []
            for i in jel:
                data = {"journal": journal_long,
                        "year": year,
                        "url": article,
                        "jel": i}
                df.append(data)
            df = pd.DataFrame(df)
            
            return df
        
        except AttributeError:
            pass


    def save_data(self, issue: str, article: str, path: str, journal: str, journal_long: str):
        """journal (journal long):
            - app (American Economic Journal: Applied Economics)
            - aer (American Economic Review)
            - jel (Journal of Economic Literature)
            - jep (Journal of Economic Perspectives)
            - mac (American Economic Journal: Macroeconomics)
            - pol (American Economic Journal: Economic Policy)
        """

        issue = issue.split("/")[-1]
        data = []

        for i in article: data.append(self.get_jel(i, journal_long))
        
        df = pd.concat(data, sort=False).reset_index(drop=True)
        df.to_csv(f"{path}/{journal}-{issue}.csv", index=False, sep=";")


class AnnualReview:
    def get_issue(self):
        url = "https://www.annualreviews.org/content/journals/economics/browse?page=previous-issues"
        html = scrape.get_html(url=url)
        issue = [x["href"] for x in html.select(".issueBar > div:nth-child(1) > div:nth-child(2)")[0].find_all("a")]
        issue = [f"https://www.annualreviews.org{x}" for x in issue]

        return issue
    

    def get_article(self, issue: str):
        html = scrape.get_html(url=issue)
        article = [x["href"] for x in html.find_all("a", {"class": "externallink"})]
        
        return article
    

    def get_jel(self, article: str):
        pass


    def save_data(self, issue: str, article: str, path: str):
            pass


class Springer:
    def get_issue(self, journal):
        """journal (journal_long):
            - 148 (Journal of Population Economics)
            - 181 (Empirical Economics)
            - 182 (International Journal of Game Theory)
            - 191 (Journal of Evolutionary Economics)
            - 199 (Economic Theory)
            - 780 (Finance and Stochastics)
            - 10290 (Review of World Economics)
            - 10551 (Journal of Business Ethics)
            - 10640 (Environmental & Resource Economics)
            - 10683 (Experimental Economics)
            - 10693 (Journal of Financial Services Research)
            - 10797 (International Tax and Public Finance)
            - 10887 (Journal of Economic Growth)
            - 10888 (The Journal of Economic Inequality)
            - 11123 (Journal of Productivity Analysis)
            - 11127 (Public Choice)
            - 11129 (Quantitative Marketing and Economics)
            - 11146 (The Journal of Real Estate Finance and Economics)
            - 11149 (Journal of Regulatory Economics)
            - 11166 (Journal of Risk and Uncertainty)
            - 11187 (Small Business Economics)
            - 40174 (IZA Journal of European Labor Studies)
            - 40881 (Journal of the Economic Science Association)
        """

        try:
            url = f"https://link.springer.com/journal/{journal}/volumes-and-issues"
            html = scrape.get_html(url=url)
            issue = html.select("ul.u-list-reset:nth-child(2)")[0]
            issue = [x["href"] for x in issue.find_all("a")]
            issue = [f"https://link.springer.com{x}" for x in issue]

            return issue
        
        except IndexError:
            pass
    

    def get_article(self, issue: str):
        try:
            html = scrape.get_html(url=issue)
            article = [x["href"] for x in html.select("ol.u-list-reset")[0].find_all("a")]
            
            return article

        except AttributeError:
            pass
    

    def get_jel(self, article: str, journal_long: str):
        """journal (journal_long):
            - 148 (Journal of Population Economics)
            - 181 (Empirical Economics)
            - 182 (International Journal of Game Theory)
            - 191 (Journal of Evolutionary Economics)
            - 199 (Economic Theory)
            - 780 (Finance and Stochastics)
            - 10290 (Review of World Economics)
            - 10551 (Journal of Business Ethics)
            - 10640 (Environmental & Resource Economics)
            - 10683 (Experimental Economics)
            - 10693 (Journal of Financial Services Research)
            - 10797 (International Tax and Public Finance)
            - 10887 (Journal of Economic Growth)
            - 10888 (The Journal of Economic Inequality)
            - 11123 (Journal of Productivity Analysis)
            - 11127 (Public Choice)
            - 11129 (Quantitative Marketing and Economics)
            - 11146 (The Journal of Real Estate Finance and Economics)
            - 11149 (Journal of Regulatory Economics)
            - 11166 (Journal of Risk and Uncertainty)
            - 11187 (Small Business Economics)
            - 40174 (IZA Journal of European Labor Studies)
            - 40881 (Journal of the Economic Science Association)
        """

        html = scrape.get_html(url=article)

        try:
            jel = [x.text for x in html.select("ul.c-article-subject-list:nth-child(9)")[0].find_all("li")]
            year = html.select("ul.c-article-identifiers:nth-child(4)")[0].text.split("(")[1][:4]
            df = []
            for i in jel:
                data = {"journal": journal_long,
                        "year": year,
                        "url": article,
                        "jel": i}
                df.append(data)
            df = pd.DataFrame(df)
            
            return df
        
        except AttributeError:
            pass
        except IndexError:
            pass


    def save_data(self, issue: str, article: str, path: str, journal: str, journal_long: str):
        """journal (journal_long):
            - 148 (Journal of Population Economics)
            - 181 (Empirical Economics)
            - 182 (International Journal of Game Theory)
            - 191 (Journal of Evolutionary Economics)
            - 199 (Economic Theory)
            - 780 (Finance and Stochastics)
            - 10290 (Review of World Economics)
            - 10551 (Journal of Business Ethics)
            - 10640 (Environmental & Resource Economics)
            - 10683 (Experimental Economics)
            - 10693 (Journal of Financial Services Research)
            - 10797 (International Tax and Public Finance)
            - 10887 (Journal of Economic Growth)
            - 10888 (The Journal of Economic Inequality)
            - 11123 (Journal of Productivity Analysis)
            - 11127 (Public Choice)
            - 11129 (Quantitative Marketing and Economics)
            - 11146 (The Journal of Real Estate Finance and Economics)
            - 11149 (Journal of Regulatory Economics)
            - 11166 (Journal of Risk and Uncertainty)
            - 11187 (Small Business Economics)
            - 40174 (IZA Journal of European Labor Studies)
            - 40881 (Journal of the Economic Science Association)
        """

        try:
            issue = issue.split("/")[-1]
            data = []

            for i in article: data.append(self.get_jel(i, journal_long))
            
            df = pd.concat(data, sort=False).reset_index(drop=True)
            df.to_csv(f"{path}/{journal}-{issue}.csv", index=False, sep=";")
        except ValueError:
            pass


class QJE:
    def get_issue(self):
        url = "https://academic.oup.com/qje/issue-archive"
        html = scrape.get_html(url=url)
        issue = [x["href"] for x in html.select(".widget-IssueYears")[0].find_all("a")]
        issue = [f"https://academic.oup.com{x}" for x in issue]
        issues = []
        for i in issue[-2:]:
            html = scrape.get_html(url=i)
            time_interval = randint(0, 10)
            sleep(time_interval)
            issue = [x["href"] for x in html.select(".issue-covers-main-column")[0].find("ul").find_all("a")]
            for j in issue:
                j = f"https://academic.oup.com{j}"
                issues.append(j)

        return issues


    def get_article(self, issue: str):
        html = scrape.get_html(url=issue)
        time_interval = randint(0, 10)
        sleep(time_interval)
        article = [x["href"] for x in html.find_all("a", {"class": "at-articleLink"})]
        article = [f"https://academic.oup.com{x}" for x in article]

        return article


    def get_jel(self, article: str):
        html = scrape.get_html(url=article)
        time_interval = randint(0, 10)
        sleep(time_interval)

        try:
            jel = [x.text for x in html.select(".article-metadata")[0].find_all("a")]
            jel = [x.split(" -")[0] for x in jel]
            year = html.select(".ii-pub-date")[0].text.strip().split(" ")[1]
            df = []

            for i in jel:
                data = {"journal": "Quarterly Journal of Economics",
                        "year": year,
                        "url": article,
                        "jel": i}
                df.append(data)

            df = pd.DataFrame(df)

            return df
        except IndexError:
            pass
    

    def save_data(self, issue: str, article: str, path: str):
        issue = "-".join(issue.split("/")[-2:])
        data = []

        for i in article: data.append(self.get_jel(i))
        
        df = pd.concat(data, sort=False).reset_index(drop=True)
        df.to_csv(f"{path}/qje-{issue}.csv", index=False, sep=";")
