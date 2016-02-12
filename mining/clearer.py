# -*- coding: utf-8 -*-

import sys,os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

import time
import cmdln
from tools.mysql import getDB

class Clearer(cmdln.Cmdln):
    name = "clear"

    @cmdln.option("-t", "--time",
                  help="1w 1d 1h ?")
    @cmdln.option("-v", "--verbose", action="store_true",
                  help="print extra information")
    def do_filter(self, subcmd, opts, *paths):
        """${cmd_name}: filter the source data by default rules

        ${cmd_usage}
        ${cmd_option_list}
        """
        factor = 1
        if opts.time == '1w':
            factor = 7

        sql = 'select id,' \
              'source,title,content,images, ' \
              'source_view+view_number vn, source_like+like_number ln, ' \
              'source_unlike+unlike_number uln, comment_number+source_comment cn,' \
              'ctime, ' \
              'source_view+view_number , source_like+like_number ln, ' \
              'source_unlike+unlike_number uln, comment_number+source_comment' \
              ' from joke where ctime >= %s'
        db = getDB()


        timestamp = int(time.time() - 7 * 24 * 60 * 60 * factor)

        jokes = db.query_tuple(sql, timestamp)()
        ret = []
        for j in jokes:
            ret.append(j)

        insert = 'insert clean_article (id,source,title,content,images,view_number,like_number,unlike_number,comment_number,ctime) ' \
                 'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update view_number=%s,like_number=%s,unlike_number=%s,comment_number=%s'

        if ret:
            for joke in ret:
                db.insert(insert,*joke)
        else:
            print 'not result.'


if __name__ == "__main__":
    clear = Clearer()
    sys.exit(clear.main())
