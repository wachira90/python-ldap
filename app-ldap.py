import sys
import ldap


DN = "john@example.com"
secret = "pass1234"
un = "wachira"
server = "ldap://172.20.0.6"
port = 389

base = "DC=meanet,DC=mea,DC=or,DC=th"
scope = ldap.SCOPE_SUBTREE
filter = "(&(objectClass=user)(sAMAccountName=" + un + "))"
attrs = ["*"]

l = ldap.initialize(server)
l.protocol_version = 3
l.set_option(ldap.OPT_REFERRALS, 0)
print (l.simple_bind_s(DN, secret))
r = l.search(base, scope, filter, attrs)
type, user = l.result(r, 60)
name, attrs = user[0]

print(name )

print("\n\n",attrs)

if hasattr(attrs, 'has_key') and attrs.has_key('displayName'):
    print (attrs)

sys.exit()