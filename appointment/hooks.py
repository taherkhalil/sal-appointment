# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "appointment"
app_title = "Appointment Manager"
app_publisher = "Taher khalil"
app_description = "Appointment manager with schedule calendar and all in one interface"
app_icon = "calendar"
app_color = "Blue"
app_email = "taherkhalil52@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/appointment/css/appointment.css"
# app_include_js = "/assets/appointment/js/appointment.js"

# include js, css files in header of web template
# web_include_css = "/assets/appointment/css/appointment.css"
# web_include_js = "/assets/appointment/js/appointment.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "appointment.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "appointment.install.before_install"
# after_install = "appointment.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "appointment.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	# "*": {
# 	# 	"on_update": "method",
# 	# 	"on_cancel": "method",
# 	# 	"on_trash": "method"
# 	# }
# 	"Sales Invoice" : {
# 		"on_submit": "appointment.appointment_manager.doctype.appointment.appointment.set_complete_status"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"appointment.tasks.all"
# 	],
# 	"daily": [
# 		"appointment.tasks.daily"
# 	],
# 	"hourly": [
# 		"appointment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"appointment.tasks.weekly"
# 	]
# 	"monthly": [
# 		"appointment.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "appointment.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "appointment.event.get_events"
# }

