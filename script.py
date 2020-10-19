import SQL_connect as SQL
import Parse as p

def script():
    parser = p.ParserFedresurs()
    parser.parse()
    sql = SQL.SQL('resources/config.env')
    sql.mysql_save(parser.infos)


if __name__ == "__main__":
    script()