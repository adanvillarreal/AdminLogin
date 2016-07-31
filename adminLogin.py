#!/usr/bin/env python
# encoding: UTF-8
#Todo: Signal handling for TimeoutException
from urllib2 import Request, urlopen, URLError, HTTPError, socket
import colorama
import os
import socket
from colorama import Back
import ssl
import sys
import time
from socket import error as SocketError
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
x = 0
pathList = ['host-manager/', 'host-manager/html/', 'manager/html/', 'manager/','_admin/','backoffice/','account.asp','account.cfm','account.html','account.php','acct_login/','adm.asp','adm.cfm','adm.html','adm.php','adm/','adm/admloginuser.asp','adm/admloginuser.cfm','adm/admloginuser.php','adm/index.asp','adm/index.cfm','adm/index.html','adm/index.php','adm_auth.asp','adm_auth.cfm','adm_auth.php','admin.asp','admin.cfm','admin.html','admin.php','admin/','admin/account.asp','admin/account.cfm','admin/account.html','admin/account.php','admin/admin.asp','admin/admin.cfm','admin/admin.html','admin/admin.php','admin/admin_login.asp','admin/admin_login.cfm','admin/admin_login.html','admin/admin_login.php','admin/adminLogin.asp','admin/admin-login.asp','admin/adminLogin.cfm','admin/admin-login.cfm','admin/adminLogin.html','admin/admin-login.html','admin/adminLogin.php','admin/admin-login.php','admin/controlpanel.asp','admin/controlpanel.cfm','admin/controlpanel.html','admin/controlpanel.php','admin/cp.asp','admin/cp.cfm','admin/cp.html','admin/cp.php','admin/home.asp','admin/home.cfm','admin/home.html','admin/home.php','admin/index.asp','admin/index.cfm','admin/index.html','admin/index.php','admin/login.asp','admin/login.cfm','admin/login.html','admin/login.php','admin_area/','admin_area/admin.asp','admin_area/admin.cfm','admin_area/admin.html','admin_area/admin.php','admin_area/index.asp','admin_area/index.cfm','admin_area/index.html','admin_area/index.php','admin_area/login.asp','admin_area/login.cfm','admin_area/login.html','admin_area/login.php','admin_login.asp','admin_login.cfm','admin_login.html','admin_login.php','admin1.asp','admin1.html','admin1.php','admin1/','admin2.asp','admin2.cfm','admin2.html','admin2.php','admin2/index.asp','admin2/index.cfm','admin2/index.php','admin2/login.asp','admin2/login.cfm','admin2/login.php','admin4_account/','admin4_colon/','adminarea/','adminarea/admin.asp','adminarea/admin.cfm','adminarea/admin.html','adminarea/admin.php','adminarea/index.asp','adminarea/index.cfm','adminarea/index.html','adminarea/index.php','adminarea/login.asp','adminarea/login.cfm','adminarea/login.html','adminarea/login.php','admincontrol.asp','admincontrol.cfm','admincontrol.html','admincontrol.php','admincontrol/login.asp','admincontrol/login.cfm','admincontrol/login.html','admincontrol/login.php','admincp/index.asp','admincp/index.cfm','admincp/index.html','admincp/login.asp','admincp/login.cfm','administer/','administr8.asp','administr8.html','administr8.php','administr8/','administratie/','administration.html','administration.php','administration/','administrator.asp','administrator.cfm','administrator.html','administrator.php','administrator/','administrator/account.asp','administrator/account.cfm','administrator/account.html','administrator/account.php','administrator/index.asp','administrator/index.cfm','administrator/index.html','administrator/index.php','administrator/login.asp','administrator/login.cfm','administrator/login.html','administrator/login.php','administratoraccounts/','administratorlogin.asp','administratorlogin.cfm','administratorlogin.php','administratorlogin/','administrators/','administrivia/','adminLogin.asp','admin-login.asp','adminLogin.cfm','admin-login.cfm','adminLogin.html','admin-login.html','adminLogin.php','admin-login.php','adminLogin/','adminpanel.asp','adminpanel.cfm','adminpanel.html','adminpanel.php','adminpro/','admins.asp','admins.html','admins.php','admins/','AdminTools/','admloginuser.asp','admloginuser.cfm','admloginuser.php','affiliate.asp','affiliate.cfm','affiliate.php','autologin/','banneradmin/','bbadmin/','bb-admin/','bb-admin/admin.asp','bb-admin/admin.cfm','bb-admin/admin.html','bb-admin/admin.php','bb-admin/index.asp','bb-admin/index.cfm','bb-admin/index.html','bb-admin/index.php','bb-admin/login.asp','bb-admin/login.cfm','bb-admin/login.html','bb-admin/login.php','bigadmin/','blogindex/','cadmins/','ccp14admin/','cmsadmin/','controlpanel.asp','controlpanel.cfm','controlpanel.html','controlpanel.php','controlpanel/','cp.asp','cp.cfm','cp.html','cp.php','cPanel/','cpanel_file/','customer_login/','database_administration/','directadmin/','dir-login/','ezsqliteadmin/','fileadmin.asp','fileadmin.html','fileadmin.php','fileadmin/','formslogin/','globes_admin/','home.asp','home.cfm','home.html','home.php','hpwebjetadmin/','Indy_admin/','instadmin/','irc-macadmin/','LiveUser_Admin/','login.asp','login.cfm','login.html','login.php','login_db/','login1/','loginflat/','login-redirect/','login-us/','logo_sysadmin/','Lotus_Domino_Admin/','macadmin/','manuallogin/','memberadmin.asp','memberadmin.cfm','memberadmin.php','memberadmin/','members/','memlogin/','meta_login/','modelsearch/admin.asp','modelsearch/admin.cfm','modelsearch/admin.html','modelsearch/admin.php','modelsearch/index.asp','modelsearch/index.cfm','modelsearch/index.html','modelsearch/index.php','modelsearch/login.asp','modelsearch/login.cfm','modelsearch/login.html','modelsearch/login.php','moderator.asp','moderator.cfm','moderator.html','moderator.php','moderator/','moderator/admin.asp','moderator/admin.cfm','moderator/admin.html','moderator/admin.php','moderator/login.asp','moderator/login.cfm','moderator/login.html','moderator/login.php','myadmin/','navSiteAdmin/','newsadmin/','nsw/admin/login.php','openvpnadmin/','pages/admin/admin-login.asp','pages/admin/admin-login.cfm','pages/admin/admin-login.html','pages/admin/admin-login.php','panel/','panel-administracion/','panel-administracion/admin.asp','panel-administracion/admin.cfm','panel-administracion/admin.html','panel-administracion/admin.php','panel-administracion/index.asp','panel-administracion/index.cfm','panel-administracion/index.html','panel-administracion/index.php','panel-administracion/login.asp','panel-administracion/login.cfm','panel-administracion/login.html','panel-administracion/login.php','pgadmin/','phpldapadmin/','phpmyadmin/', 'phpMyAdmin', 'phppgadmin/','phpSQLiteAdmin/','platz_login/','power_user/','project-admins/','pureadmin/','radmind/','radmind-1/','rcjakar/admin/login.php','rcLogin/','Server.asp', 'server-status', 'Server.html','Server.php','server/','server_admin_small/','ServerAdministrator/','showlogin/','simpleLogin/','siteadmin/index.asp','siteadmin/index.cfm','siteadmin/index.php','siteadmin/login.asp','siteadmin/login.cfm','siteadmin/login.html','siteadmin/login.php','smblogin/','sql-admin/','ss_vms_admin_sm/','sshadmin/','staradmin/','sub-login/','Super-Admin/','support_login/','sysadmin.asp','sysadmin.html','sysadmin.php','sysadmin/','sys-admin/','SysAdmin2/','sysadmins/','system_administration/','system-administration/','typo3/','ur-admin.asp','ur-admin.html','ur-admin.php','ur-admin/','user.asp','user.html','user.php','useradmin/','UserLogin/','utility_login/','vadmind/','vmailadmin/','webadmin.asp','webadmin.cfm','webadmin.html','webadmin.php','WebAdmin/','webadmin/admin.asp','webadmin/admin.cfm','webadmin/admin.html','webadmin/admin.php','webadmin/index.asp','webadmin/index.cfm','webadmin/index.html','webadmin/index.php','webadmin/login.asp','webadmin/login.cfm','webadmin/login.html','webadmin/login.php','wizmysqladmin/','wp-admin/','wp-login.php','wp-login/','xlogin/','yonetici.asp','yonetici.html','yonetici.php','yonetim.asp','yonetim.html','yonetim.php','panel/?a=cp']
#scanfile = open("ips.txt", "r")
scanfile = open(sys.argv[1], "r")
ofile = 'results'+sys.argv[1]+time.strftime("%m%d-%H%M%S")+'.txt'
results = open(ofile, "a")
for url in scanfile.readlines():
    x+=1
    try:
        print url + str(x)
	#in case you need to blacklist a net, include them here       
	#if '10.2.80' in url:
            continue
        for path in pathList:
            nurl= url.rstrip()+'/'+path.rstrip()
            r = Request(nurl)
            print '\t'+path
            try:
                response = urlopen(r, context=ctx, timeout=3)
                print(Back.GREEN + nurl + ' code: ' +str(response.code)+Back.RESET)
                results.write( nurl + ' code: ' +str(response.code)+"\n")
            except HTTPError as e:
                if e.code == 403:
                    print(Back.YELLOW + nurl +' code: ' +str(e.code)+ Back.RESET)
                    results.write( nurl + ' code: ' +str(e.code)+ "\n")
            except URLError as e:
                continue
            except SocketError as e:
                print Back.RED + 'Socket error' + Back.RESET
                results.write('Socket Error ' + nurl + "\n")
            except socket.timeout as e:
                print 'Socket timed out'
            except ssl.SSLError as e:
                print(Back.RED + 'SSL error ' + nurl + Back.RESET)
                results.write('SSLError ' + nurl+ "\n")
            results.close()
            results = open(ofile, "a")
    except KeyboardInterrupt as e:
        continue
