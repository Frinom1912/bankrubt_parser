import time
import sys
import parser_bankr_lib.SQL_connect as SQL
import parser_bankr_lib.Parse as p

def script():
    start_time = time.time()
    parser = p.ParserFedresurs()
    parser.parse()
    elapsed_time = time.time() - start_time
    sys.stdout.write(f"Elapsed time: {int(elapsed_time/60)} mins {int(elapsed_time-int(elapsed_time))} secs\n")
    cfg = SQL.Config("config.env")
    if cfg.get_config()["SQL"] == "False":
        for info in parser.infos:
            print(info)
            print("\n")
    else:
        sql = SQL.SQL('config.env')
        sql.mysql_save(parser.infos)


if __name__ == "__main__":
    script()