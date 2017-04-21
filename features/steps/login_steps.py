from behave import *


@when(u'a user visits the login page')
def visit_login(context):
    raise NotImplementedError(u'STEP: When a user visits the login page')


@then(u'she should see the username field')
def see_username_field(context):
    raise NotImplementedError(u'STEP: Then she should see the username field')


@then(u'she should see the password field')
def see_password_field(context):
    raise NotImplementedError(u'STEP: Then she should see the password field')


@then(u'she should see the login button')
def see_login_button(context):
    raise NotImplementedError(u'STEP: Then she should see the login button')


@when(u'she logs in with username "{username}" and password "{password}"')
def login(context, username, password):
    raise NotImplementedError(u'STEP: When she logs in with username "test" and password "test123"')


@then(u'she should see a message of login success')
def see_login_success(context):
    raise NotImplementedError(u'STEP: Then she should see a message of login success')


@then(u'she should see a message of login failure')
def see_login_failure(context):
    raise NotImplementedError(u'STEP: Then she should see a message of login failure')


@given(u'she sees the Logout link')
def see_logout_link(context):
    raise NotImplementedError(u'STEP: Given she sees the Logout link')


@when(u'she clicks on the Logout link')
def click_logout_link(context):
    raise NotImplementedError(u'STEP: When she clicks on the Logout link')


@then(u'she returns to the site')
def visit_site(context):
    raise NotImplementedError(u'STEP: Then she returns to the site')


@then(u'she sees a message telling her she has logged out')
def see_logout_success(context):
    raise NotImplementedError(u'STEP: Then she sees a message telling her she has logged out')