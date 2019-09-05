from GG_Star import *
from thrift import transport, protocol, server
from GG_Star.thrift.Thrift import *
from GG_Star.thrift.TMultiplexedProcessor import *
from GG_Star.thrift.TSerialization import *
from GG_Star.thrift.TRecursive import *
from GG_Star.thrift.protocol import TCompactProtocol
from GG_Star.thrift.transport import THttpClient
from akad.ttypes import *
from time import sleep
from threading import Thread
import pytz, datetime, time, timeit, livejson, asyncio, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib,traceback,platform
from datetime import timedelta, date
from datetime import datetime
# GG_Star™ Simple Bots
# Free To Use,All Credits Belong To Me,star
# Found Some Bugs Or Error? Feel Free To Report Bugs :)
# Login Option Below
# LINE : LINE()
# Email : LINE("email","Password")
# Auth Token : LINE("authtoken")
# Primary Token : LINE("primary",appName='IOS\t8.17.0\tstar\t11.2.5')
programStart = time.time()
cl = LINE()
print('==== UNIT 1 READY ! ====')
ki = LINE()
print('==== UNIT 2 READY ! ====')
kk = LINE()
print('==== UNIT 3 READY ! ====')
kc = LINE()
print('==== UNIT 4 READY ! ====')
km = LINE()
print('==== UNIT 5 READY ! ====')
print ('\n\nALL UNIT READY !')

mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
KAC = [ki,kk,kc,km]

loop = asyncio.get_event_loop()
status = livejson.File('status.json', True, False, 4)
with open("settings.json","r",encoding="utf-8") as fp:
	settings = json.load(fp)
creator = status["creator"]
owner = status["owner"]
admin = status["admin"]
staff = status["staff"]
mybots = status["mybots"]
Bots = [mid,Amid,Bmid,Cmid,Dmid]
Botslist = [cl,ki,kk,kc,km]
resp1 = cl.getProfile().displayName
resp2 = ki.getProfile().displayName
resp3 = kk.getProfile().displayName
resp4 = kc.getProfile().displayName
resp5 = km.getProfile().displayName

for GStar in Botslist:
	for star in Bots:
		try:
			GStar.findAndAddContactsByMid(star)
		except:
			pass

def backupData():
	try:
		backup = settings
		f = codecs.open('settings.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except:
		pass

def restartProgram():
	print('####==== PROGRAM RESTARTED ====####')
	backupData()
	python = sys.executable
	os.execl(python, python, *sys.argv)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Months" % (months)
    if weeks != 0: text += " %02d Weeks" % (weeks)
    if days != 0: text += " %02d Days" % (days)
    if hours !=  0: text +=  " %02d Hours" % (hours)
    if mins != 0: text += " %02d Minutes" % (mins)
    if secs != 0: text += " %02d Seconds" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Tehran")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def kick(grup, target):
	try:
		cl.kickoutFromGroup(grup, [target])
	except:
		try:
			ki.kickoutFromGroup(grup, [target])
		except:
			try:
				kk.kickoutFromGroup(grup, [target])
			except:
				try:
					kc.kickoutFromGroup(grup, [target])
				except:
					try:
						km.kickoutFromGroup(grup, [target])
					except:
						pass

def cancel(grup, target):
	try:
		cl.cancelGroupInvitation(grup, [target])
	except:
		try:
			ki.cancelGroupInvitation(grup, [target])
		except:
			try:
				kk.cancelGroupInvitation(grup, [target])
			except:
				try:
					kc.cancelGroupInvitation(grup, [target])
				except:
					try:
						km.cancelGroupInvitation(grup, [target])
					except:
						pass

def lockqr(grup):
	try:
		G = cl.getGroup(grup)
		G.preventedJoinByTicket = True
		cl.updateGroup(G)
	except:
		try:
			G = ki.getGroup(grup)
			G.preventedJoinByTicket = True
			ki.updateGroup(G)
		except:
			try:
				G = kk.getGroup(grup)
				G.preventedJoinByTicket = True
				kk.updateGroup(G)
			except:
				try:
					G = kc.getGroup(grup)
					G.preventedJoinByTicket = True
					kc.updateGroup(G)
				except:
					try:
						G = km.getGroup(grup)
						G.preventedJoinByTicket = True
						km.updateGroup(G)
					except:
						pass

def backup(grup, target):
	try:
		cl.inviteIntoGroup(grup, [target])
		if target == Amid:
			ki.acceptGroupInvitation(grup)
		if target == Bmid:
			kk.acceptGroupInvitation(grup)
		if target == Cmid:
			kc.acceptGroupInvitation(grup)
		if target == Dmid:
			km.acceptGroupInvitation(grup)
	except:
		try:
			ki.inviteIntoGroup(grup, [target])
			if target == mid:
				cl.acceptGroupInvitation(grup)
			if target == Bmid:
				kk.acceptGroupInvitation(grup)
			if target == Cmid:
				kc.acceptGroupInvitation(grup)
			if target == Dmid:
				km.acceptGroupInvitation(grup)
		except:
			try:
				kk.inviteIntoGroup(grup, [target])
				if target == mid:
					cl.acceptGroupInvitation(grup)
				if target == Amid:
					ki.acceptGroupInvitation(grup)
				if target == Cmid:
					kc.acceptGroupInvitation(grup)
				if target == Dmid:
					km.acceptGroupInvitation(grup)
			except:
				try:
					kc.inviteIntoGroup(grup, [target])
					if target == mid:
						cl.acceptGroupInvitation(grup)
					if target == Amid:
						ki.acceptGroupInvitation(grup)
					if target == Bmid:
						kk.acceptGroupInvitation(grup)
					if target == Dmid:
						km.acceptGroupInvitation(grup)
				except:
					try:
						km.inviteIntoGroup(grup, [target])
						if target == mid:
							cl.acceptGroupInvitation(grup)
						if target == Amid:
							ki.acceptGroupInvitation(grup)
						if target == Bmid:
							kk.acceptGroupInvitation(grup)
						if target == Cmid:
							kc.acceptGroupInvitation(grup)
					except:
						pass

def invite(grup, target):
	try:
		cl.findAndAddContactsByMid(target)
		cl.inviteIntoGroup(grup, [target])
	except:
		try:
			ki.findAndAddContactsByMid(target)
			ki.inviteIntoGroup(grup, [target])
		except:
			try:
				kk.findAndAddContactsByMid(target)
				kk.inviteIntoGroup(grup, [target])
			except:
				try:
					kc.findAndAddContactsByMid(target)
					kc.inviteIntoGroup(grup, [target])
				except:
					try:
						km.findAndAddContactsByMid(target)
						km.inviteIntoGroup(grup, [target])
					except:
						pass

def blacklist(target):
	try:
		if target in creator or target in owner or target in admin or target in staff or target in mybots or target in Bots:
			pass
		else:
			status["blacklist"].append(target)
	except:
		pass

def logspeed():
	get_profile_time_start = time.time()
	get_profile = cl.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = ki.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = kk.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = kc.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = km.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)

def command(text):
	vyna = text.lower()
	if settings['setKey']['status']:
		if vyna.startswith(settings['setKey']['key']):
			cmd = vyna.replace(settings['setKey']['key'],'')
		else:
			cmd = 'Undefined command'
	else:
		cmd = text.lower()
	return cmd

def removeCmd(text, key=''):
	if key == '':
		setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
	else:
		setKey = key
	text_ = text[len(setKey):]
	sep = text_.split(' ')
	return text_[len(sep[0] + ' '):]

def commands():
	key = '' if not settings['setKey']['status'] else settings['setKey']['key']
	with open('help.txt', 'r') as f:
		text = f.read()
	helpMessage = text.format(key=key.title())
	return helpMessage

def RECEIVE_MESSAGE(op):
	global cmd
	global text
	global groupParam
	msg = op.message
	text = msg.text
	reply = msg.id
	receiver = msg.to
	sender = msg._from
	if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
		if msg.toType == 0:
			if sender != cl.profile.mid:
				to = sender
			else:
				to = receiver
		if msg.toType == 1:
			to = receiver
		if msg.toType == 2:
			to = receiver
		if msg.contentType == 1:
			if sender in creator or sender in owner:
				if mid in settings["GG_StarPict"]:
					path = cl.downloadObjectMsg(msg.id)
					del settings["GG_StarPict"][mid]
					cl.updateProfilePicture(path)
					cl.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if Amid in settings["GG_StarPict"]:
					path = ki.downloadObjectMsg(msg.id)
					del settings["GG_StarPict"][Amid]
					ki.updateProfilePicture(path)
					ki.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if Bmid in settings["GG_StarPict"]:
					path = kk.downloadObjectMsg(msg.id)
					del settings["GG_StarPict"][Bmid]
					kk.updateProfilePicture(path)
					kk.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if Cmid in settings["GG_StarPict"]:
					path = kc.downloadObjectMsg(msg.id)
					del settings["GG_StarPict"][Cmid]
					kc.updateProfilePicture(path)
					kc.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if Dmid in settings["GG_StarPict"]:
					path = km.downloadObjectMsg(msg.id)
					del settings["GG_StarPict"][Dmid]
					km.updateProfilePicture(path)
					km.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
		if msg.contentType == 0:
			if text is None:
				return
			else:
				GG_Star = command(text)
				GStar = " ".join(GG_Star.split())
			for GStar in GG_Star.split(' & '):
				if GStar == "help":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						cl.sendReplyMessage(reply,receiver,commands())
						cl.sendReplyMessage(reply,receiver,"Note:\nFor Multi Command\nMust Use & Between First and Second Command\nExample Below:\nHelp & Speed")
				elif GStar == "reboot":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						cl.sendReplyMessage(reply,receiver,"「 Please Wait... 」")
						settings["restartPoint"] = receiver
						restartProgram()
				elif GStar == "clearchat":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						for a in Botslist:
							a.removeAllMessages(op.param2)
						for u in Botslist:
							u.sendReplyMessage(reply,receiver,"「 All Chat Cleared 」")
				elif GStar == "respon":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						cl.sendReplyMessage(reply,receiver,"「 {} 」".format(resp1))
						ki.sendReplyMessage(reply,receiver,"「 {} 」".format(resp2))
						kk.sendReplyMessage(reply,receiver,"「 {} 」".format(resp3))
						kc.sendReplyMessage(reply,receiver,"「 {} 」".format(resp4))
						km.sendReplyMessage(reply,receiver,"「 {} 」".format(resp5))
				elif GStar == "speed":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						cl.sendReplyMessage(reply,receiver,logspeed())
						ki.sendReplyMessage(reply,receiver,logspeed())
						kk.sendReplyMessage(reply,receiver,logspeed())
						kc.sendReplyMessage(reply,receiver,logspeed())
						km.sendReplyMessage(reply,receiver,logspeed())
				elif GStar == "byeall":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						for bot in Botslist:
							bot.leaveGroup(receiver)
				elif GStar == "inviteall":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						try:
							cl.inviteIntoGroup(receiver, [Amid,Bmid,Cmid,Dmid])
							ki.acceptGroupInvitation(receiver)
							kk.acceptGroupInvitation(receiver)
							kc.acceptGroupInvitation(receiver)
							km.acceptGroupInvitation(receiver)
						except TalkException as talk_error:
							if talk_error.code == 35:
								G = cl.getGroup(receiver)
								G.preventedJoinByTicket = False
								cl.updateGroup(G)
								links = cl.reissueGroupTicket(receiver)
								for bot in KAC:
									bot.acceptGroupInvitationByTicket(receiver,links)
								G = cl.getGroup(receiver)
								G.preventedJoinByTicket = True
								cl.updateGroup(G)
				elif GStar == "blacklist" or GStar == "banlist":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						if len(status["blacklist"]) > 0:
							h = [a for a in status["blacklist"]]
							k = len(h)//20
							for aa in range(k+1):
								if aa == 0:dd = '「 Blacklist User 」';no=aa
								else:dd = '';no=aa*20
								msgas = dd
								for a in h[aa*20:(aa+1)*20]:
									no+=1
									if no == len(h):msgas+='\n{}. @!'.format(no)
									else:msgas += '\n{}. @!'.format(no)
								sendMention(to, msgas, h[aa*20:(aa+1)*20])
						else:
							cl.sendReplyMessage(reply,receiver,"「 Doesn't Have Any Blacklist User -_- 」")
				elif GStar == "clearban":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						if len(status["blacklist"]) > 0:
							cl.sendReplyMessage(reply,receiver, "「 {} User Cleared 」".format(len(status["blacklist"])))
							status["blacklist"].clear()
						else:
							cl.sendReplyMessage(reply,receiver,"「 Doesn't Have Any Blacklist User -_- 」")
				elif GStar == "squad list":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						ma = ""
						a = 0
						for anu in mybots:
							a = a + 1
							end = '\n'
							ma += '┣ ' + str(a) + ". " +cl.getContact(anu).displayName + "\n"
						cl.sendReplyMessage(reply,receiver, "┏━ GG_STAR ™\n┣━━━━ List Bots\n"+ma+"┗━ Total「%s」Bots" %(str(len(mybots))))
				elif GStar == "view bots":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						ma = ""
						a = 0
						for anu in Bots:
							a = a + 1
							end = '\n'
							ma += '┣ ' + str(a) + ". " +cl.getContact(anu).displayName + "\n"
						cl.sendReplyMessage(reply,receiver, "┏━ GG_STAR™\n┣━━━━ List Bots\n"+ma+"┗━ Total「%s」Bots" %(str(len(Bots))))
				elif GStar == "view access":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						ma = ""
						mb = ""
						mc = ""
						md = ""
						a = 0
						b = 0
						c = 0
						d = 0
						for anu in creator:
							a = a + 1
							end = '\n'
							ma += '┣ ' + str(a) + ". " +cl.getContact(anu).displayName + "\n"
						for anu in owner:
							b = b + 1
							end = '\n'
							mb += '┣ ' + str(b) + ". " +cl.getContact(anu).displayName + "\n"
						for anu in admin:
							c = c + 1
							end = '\n'
							mc += '┣ ' + str(c) + ". " +cl.getContact(anu).displayName + "\n"
						for anu in staff:
							d = d + 1
							end = '\n'
							md += '┣ ' + str(d) + ". " +cl.getContact(anu).displayName + "\n"
						cl.sendReplyMessage(msg.id, to, "┏╸GG_STAR ™\n┣━━━━ List Access\n┣━━━━ Creator\n"+ma+"┣━━━━ Owner\n"+mb+"┣━━━━ Admin\n"+mc+"┣━━━━ Staff\n"+md+"┗━ Total「%s」Access" %(str(len(creator)+len(owner)+len(admin)+len(staff))))
				elif GStar.startswith("add owner"):
					if sender in creator:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["owner"].append(target)
								sendMention(to,"「 Add Owner 」\nUser @! Added To Owner Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Owner 」\nCreator Permission -_-")
				elif GStar.startswith("del owner"):
					if sender in creator:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["owner"].remove(target)
								sendMention(to,"「 Delete Owner 」\nUser @! Deleted From Owner Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Owner 」\nCreator Permission -_-")
				elif GStar.startswith("add admin"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["admin"].append(target)
								sendMention(to,"「 Add Admin 」\nUser @! Added To Admin Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Admin 」\nOwner Permission -_-")
				elif GStar.startswith("del admin"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["admin"].remove(target)
								sendMention(to,"「 Delete Admin 」\nUser @! Deleted From Admin Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Admin 」\nOwner Permission -_-")
				elif GStar.startswith("add staff"):
					if sender in creator or sender in owner or sender in admin:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["staff"].append(target)
								sendMention(to,"「 Add Staff 」\nUser @! Added To Staff Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Staff 」\nOwner/Admin Permission -_-")
				elif GStar.startswith("del staff"):
					if sender in creator or sender in owner or sender in admin:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["staff"].remove(target)
								sendMention(to,"「 Delete Staff 」\nUser @! Deleted From Staff Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Staff 」\nOwner/Admin Permission -_-")
				elif GStar.startswith("add squad"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["mybots"].append(target)
								sendMention(to,"「 Add Squad 」\nUser @! Added To Squad List ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Squad 」\nOwner Permission -_-")
				elif GStar.startswith("del squad"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["mybots"].remove(target)
								sendMention(to,"「 Delete Squad 」\nUser @! Deleted From Squad List ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Squad 」\nOwner Permission -_-")
				elif GStar.startswith("add ban"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["blacklist"].append(target)
								sendMention(to,"「 Add Blacklist 」\nUser @! Added To Blacklist User",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Blacklist 」\nOwner Permission -_-")
				elif GStar.startswith("del ban"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["blacklist"].remove(target)
								sendMention(to,"「 Delete Blacklist 」\nUser @! Deleted From Blacklist User",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Blacklist 」\nOwner Permission -_-")
				elif GStar.startswith("lock group "):
					if sender in creator or sender in owner or sender in admin or sender in staff:
						spl = GStar.replace("lock group ","")
						if spl == "on":
							if receiver in status["lock"]:
								GStar = "Group Already Locked -_-"
							else:
								status["lock"].append(receiver)
								GStar = "Owkayy,Group Locked Now~"
							cl.sendReplyMessage(reply,receiver,"「 Lock Group 」\n" + GStar)
						if spl == "off":
							if receiver in status["lock"]:
								status["lock"].remove(receiver)
								GStar = "Owkayy,Group Unlocked Now~"
							else:
								GStar = "Group Already Unlocked -_-"
							cl.sendReplyMessage(reply,receiver,"「 Lock Group 」\n" + GStar)
				elif GStar.startswith("checkbot"):
					if sender in creator or sender in owner or sender in admin or sender in staff:
						try:cl.inviteIntoGroup(to, ["uef0c143093598fe6c61ba50dea07102e"]);has = "OK"
						except:has = "NOT"
						try:cl.kickoutFromGroup(to, ["uef0c143093598fe6c61ba50dea07102e"]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "Normal~"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "Normal~"
						else:sil1 = "Down!"
						cl.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:ki.inviteIntoGroup(to, ["u62a0fe51069223e123f54514082c40e4"]);has = "OK"
						except:has = "NOT"
						try:ki.kickoutFromGroup(to, ["u62a0fe51069223e123f54514082c40e4"]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "Normal~"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "Normal~"
						else:sil1 = "Down!"
						ki.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:kk.inviteIntoGroup(to, ["ub7b2ac795682db396f079a7c65150f3b"]);has = "OK"
						except:has = "NOT"
						try:kk.kickoutFromGroup(to, ["ub7b2ac795682db396f079a7c65150f3b"]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "Normal~"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "Normal~"
						else:sil1 = "Down!"
						kk.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:kc.inviteIntoGroup(to, ["u04c7b68b1b3d83a75a39caa5c296273a"]);has = "OK"
						except:has = "NOT"
						try:kc.kickoutFromGroup(to, ["u04c7b68b1b3d83a75a39caa5c296273a"]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "Normal~"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "Normal~"
						else:sil1 = "Down!"
						kc.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:km.inviteIntoGroup(to, ["u5bdf07700739f800d4d29f908ab23631"]);has = "OK"
						except:has = "NOT"
						try:km.kickoutFromGroup(to, ["u5bdf07700739f800d4d29f908ab23631"]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "Normal~"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "Normal~"
						else:sil1 = "Down!"
						km.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
				elif GStar.startswith("changename:1 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname = cl.getProfile()
							dname.displayName = name
							cl.updateProfile(dname)
							cl.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						cl.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changename:2 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname = ki.getProfile()
							dname.displayName = name
							ki.updateProfile(dname)
							ki.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						ki.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changename:3 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname = kk.getProfile()
							dname.displayName = name
							kk.updateProfile(dname)
							kk.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						kk.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changename:4 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname = kc.getProfile()
							dname.displayName = name
							kc.updateProfile(dname)
							kc.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						kc.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changename:5 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname = km.getProfile()
							dname.displayName = name
							km.updateProfile(dname)
							km.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						km.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changename:all "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname1 = cl.getProfile()
							dname1.displayName = name
							cl.updateProfile(dname1)
							cl.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname2 = ki.getProfile()
							dname2.displayName = name
							ki.updateProfile(dname2)
							ki.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname3 = kk.getProfile()
							dname3.displayName = name
							kk.updateProfile(dname3)
							kk.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname4 = kc.getProfile()
							dname4.displayName = name
							kc.updateProfile(dname4)
							kc.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname5 = km.getProfile()
							dname5.displayName = name
							km.updateProfile(dname5)
							km.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						for a in Botslist:
							a.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changebio:1 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio = cl.getProfile()
							bio.statusMessage = name
							cl.updateProfile(bio)
							cl.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						cl.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changebio:2 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio = ki.getProfile()
							bio.statusMessage = name
							ki.updateProfile(bio)
							ki.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						ki.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changebio:3 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio = kk.getProfile()
							bio.statusMessage = name
							kk.updateProfile(bio)
							kk.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						kk.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changebio:4 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio = kc.getProfile()
							bio.statusMessage = name
							kc.updateProfile(bio)
							kc.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						kc.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changebio:5 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio = km.getProfile()
							bio.statusMessage = name
							km.updateProfile(bio)
							km.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						km.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changebio:all "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio1 = cl.getProfile()
							bio1.statusMessage = name
							cl.updateProfile(bio1)
							cl.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio2 = ki.getProfile()
							bio2.statusMessage = name
							ki.updateProfile(bio2)
							ki.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio3 = kk.getProfile()
							bio3.statusMessage = name
							kk.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio4 = kc.getProfile()
							bio4.statusMessage = name
							kc.updateProfile(bio4)
							kc.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio5 = km.getProfile()
							bio5.statusMessage = name
							km.updateProfile(bio5)
							km.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						for a in Botslist:
							a.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("changepict:"):
					if sender in creator or sender in owner:
						spl = GStar.replace("changepict:","")
						if spl == "1":
							settings["GG_StarPict"][mid] = True
							cl.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "2":
							settings["GG_StarPict"][Amid] = True
							ki.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "3":
							settings["GG_StarPict"][Bmid] = True
							kk.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "4":
							settings["GG_StarPict"][Cmid] = True
							kc.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "5":
							settings["GG_StarPict"][Dmid] = True
							km.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "all":
							settings["GG_StarPict"][mid] = True
							settings["GG_StarPict"][Amid] = True
							settings["GG_StarPict"][Bmid] = True
							settings["GG_StarPict"][Cmid] = True
							settings["GG_StarPict"][Dmid] = True
							for a in Botslist:
								a.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
					else:
						cl.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nAccess Limited For Owner Only -_-")
				elif GStar.startswith("kick"):
					if sender in creator or sender in owner or sender in admin or sender in staff:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							if target in creator or target in owner or target in admin or target in staff or target in Bots or target in mybots:
								pass
							else:
								try:
									hihi = threading.Thread(target=blacklist, args=(target,)).start()
									huhu = threading.Thread(target=kick, args=(receiver, target)).start()
								except:
									pass

async def cerberusRun():
	if settings["restartPoint"] is not None:
		res = "「 Hello Im Back ^_^ 」"
		targets = cl.getGroupIdsJoined()
		for target in targets:
			try:
				cl.sendMessage(target, res)
			except TalkException:
				pass
			settings["restartPoint"] = None
	while 1:
		try:
			en = cl.poll.fetchOperations(cl.revision, 50)
			for op in en:
				if op.type != 0:
					cl.revision = max(cl.revision, op.revision)
					if op.type == 11:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								wew = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									wew1 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew2 = threading.Thread(target=lockqr, args=(op.param1,)).start()
								except:
									pass
						if op.param2 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									wew3 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew4 = threading.Thread(target=lock, args=(op.param1,)).start()
								except:
									pass
						if op.param3 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									wew5 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew6 = threading.Thread(target=lock, args=(op.param1,)).start()
								except:
									pass
					if op.type == 13:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								wew7 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									wew8 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew9 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param2 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									wew10 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew11 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									wew12 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew13 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
								except:
									pass
						if mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									cl.acceptGroupInvitation(op.param1)
								else:
									cl.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									cl.leaveGroup(op.param1)
						if Amid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									ki.acceptGroupInvitation(op.param1)
								else:
									ki.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									ki.leaveGroup(op.param1)
						if Bmid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									kk.acceptGroupInvitation(op.param1)
								else:
									kk.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									kk.leaveGroup(op.param1)
						if Cmid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									kc.acceptGroupInvitation(op.param1)
								else:
									kc.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									kc.leaveGroup(op.param1)
						if Dmid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									km.acceptGroupInvitation(op.param1)
								else:
									km.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									km.leaveGroup(op.param1)
					if op.type == 17:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									wew14 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew15 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								except:
									pass
						if op.param2 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									wew16 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
					if op.type == 19:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								wew17 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									wew18 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								wew19 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									wew20 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew21 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									wew22 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in Amid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								wew23 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									wew24 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									wew25 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									wew26 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in Bmid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn1 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn2 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									rdwn3 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in Cmid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn4 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn5 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn6 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									rdwn7 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in Dmid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn8 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn9 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn10 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									rdwn11 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
					if op.type == 32:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn12 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn13 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 == mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn14 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn15 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn16 = threading.Threas(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 == Amid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn17 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn18 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn19 = threading.Threas(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 == Bmid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn20 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn21 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn22 = threading.Threas(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 == Cmid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn23 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn24 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn25 = threading.Threas(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 == Dmid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								rdwn26 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									rdwn27 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									rdwn28 = threading.Threas(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
					if op.type == 26:
						RECEIVE_MESSAGE(op)
		except Exception as error:
			error = traceback.format_exc()
			if "EOFError" in error:
				pass
			elif "log_out" in error.lower():
				backupData()
				time.sleep(5)
				python = sys.executable
				os.execl(python, python, *sys.argv)
			elif "ShouldSyncException" in error:
				backupData()
				logError(error)
				time.sleep(5)
				python3 = sys.executable
				os.execl(python3, python3, *sys.argv)
			elif "TalkException(code=8, reason='LOG_OUT', parameterMap=None)" in error:
				backupData()
				logError(error)
				time.sleep(5)
				python = sys.executable
				os.execl(python, python, *sys.argv)
			elif "TalkException(code=20, reason='[UNCAUGHT_INTERNAL_ERROR] [UNCAUGHT_INTERNAL_ERROR] Login from secondary user blocked by userHash + clientType 8cb91561b450b38ccf0119fc4f5e37a3MA', parameterMap=None)" in error:
				backupData()
				logError(error)
				time.sleep(5)
				python = sys.executable
				os.execl(python, python, *sys.argv)
			else:
				traceback.print_exc()
				logError(error)
if __name__ == '__main__':
	print('####==== PROGRAM STARTED ====####')
	threading.Thread(target=loop.run_until_complete(cerberusRun())).start()