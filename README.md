# test-web-amazon

Web automation testing demo using Selenium webdriver and Python

<b>Test Environments:</b>
<ul>
<li>Windows 10 Home
<li>Google Chrome (64 bit) Version 84.0
<li>Python 3.7.6
<li>Selenium 3.141.0
</ul>

<b>Setup:</b>
<ol>
<li>Install Python from https://www.python.org/downloads/. Select option to add Python to PATH during the installation.
<li>Clone or download code from this repository
<li>Create virtual Environments in the location where the code reside locally
    <br><code>pip install virtualenv</code>
    <br><code>pip install virtualenvwrapper-win</code>
    <br><code>mkvirtualenv amazon</code>
    <br><code>pip install selenium</code>
    <br><code>pip install html-testRunner</code>
<li>Download Chrome web driver (chromedriver_win32.zip) from https://sites.google.com/a/chromium.org/chromedriver/ and ensure chromedriver.exe location is added to the PATH environment variable in the virtual environment.
</ol>

<b>Run Test on windows:</b>
<ol>    
    <li>Launch command line prompt
    <li>Switch to amazon virtual environment: <code>workon amazon</code>
    <li>Run test cases: <code>python tests\TestCases.py
</ol>
        
<b>Reference:</b>
<ul>
<li>https://docs.python.org/3/library/unittest.html
<li>https://medium.com/@asheeshmisra29/web-automation-selenium-webdriver-and-python-getting-started-part-1-157be93049d7
</ul>
