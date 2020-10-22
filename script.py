import SQL_connect as SQL
import Parse as p
import time
import sys


def script():
    start_time = time.time()
    parser = p.ParserFedresurs()
    parser.parse()
    elapsed_time = time.time() - start_time
    sys.stdout.write(f"Elapsed time: {int(elapsed_time/60)} mins {int(elapsed_time-int(elapsed_time))} secs\n")
    sql = SQL.SQL('resources/config.env')
    sql.mysql_save(parser.infos)


if __name__ == "__main__":
    script()