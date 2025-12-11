Make an account with password `/srv/app/data/uids`.

When you login, input the uid as `<uid> /srv/app/data/uids`.

Due to lack of quoting, `input_uid` undergoes word expansion and login is successful:
```
./login.py $input_uid $input_passwd
```

Now `uid` is `<uid> /srv/app/data/uids`, now abuse word expansion again by deleting account:
```
rm -f /srv/app/data/passwd/$uid.txt
```

This will delete `/srv/app/data/uids.txt`.

Now just register a new account, and it will be first in the list. Log out and log back in, and you will be admin.
