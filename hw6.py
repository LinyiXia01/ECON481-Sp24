## Exercise 0
def github(): 
    """
    This function returns a link to my solutions on GitHub.
    """    
    return "https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw6.py"

github()


import sqlalchemy
from sqlalchemy import create_engine

path = 'auctions.db'
engine = create_engine(f'sqlite:///{path}')

from sqlalchemy import inspect

inspector = inspect(engine)
inspector.get_table_names()

import pandas as pd
from sqlalchemy.orm import Session

class DataBase:
    def __init__(self, loc: str, db_type: str = "sqlite") -> None:
        """Initialize the class and connect to the database"""
        self.loc = loc
        self.db_type = db_type
        self.engine = create_engine(f'{self.db_type}:///{self.loc}')
    def query(self, q: str) -> pd.DataFrame:
        """Run a query against the database and return a DataFrame"""
        with Session(self.engine) as session:
            df = pd.read_sql(q, session.bind)
        return(df)
    def execute(self, q: str) -> None:
        """Execute statement on the database"""
        with self.engine.connect() as conn:
            conn.execute(text(q))

auctions = DataBase(path)


### Exercise 1

def std() -> str:
    """
    This function takes no arguments and returns a string containing a SQL query 
    that can be run against the auctions.db database that outputs a table with two columns: itemId and 
    std, the standard deviation of bids for that item.
    """
    q = """
    with avg_bids as(
    select 
     itemId
     ,bidamount
     ,avg(bidamount) over (partition by itemId) as avg_bid
    from bids
    )

    select itemId, 
    case when count(itemId) > 1 then 
    sqrt(
        sum(
            (bidamount - avg_bid) * 
            (bidamount - avg_bid)
        ) / (count(itemId) - 1)
    )
    else
    NULL 
    end as std 
    from avg_bids
    group by itemId;
    """
    return q

q1 = std()
print(auctions.query(q1))


## Exercise 2
def bidder_spend_frac() -> str:
    """
    This function takes no arguments and returns a string containing a SQL query that 
    can be run against the auctions.db database that outputs a table that has four columns":
    'bidderName','total_spend','total_bids','spend_frac'.
    """
    q = """
    select 
     b.bidderName
     ,sum(case when b.highBidderName = b.bidderName then b.bidAmount else 0 end) as total_spend
     ,sum(b.bidAmount) as total_bids
     ,cast(sum(case when b.highBidderName = b.bidderName then b.bidamount else 0 end) as real) / cast(sum(b.bidamount) as real) as spend_frac
    from bids as b
    join (
        select bidderName, itemId, max(bidAmount) as max_bid
        from bids
        group by bidderName, itemId
    ) as max_bids
    on b.bidderName = max_bids.bidderName and b.itemId = max_bids.itemId and b.bidAmount = max_bids.max_bid
    group by b.bidderName;
    """
    return q

q2 = bidder_spend_frac()
print(auctions.query(q2))


## Exercise 3
def min_increment_freq() -> str:
    """
    This function takes no arguments and 
    returns a string containing a SQL query that 
    can be run against the auctions.db database that 
    outputs a table that has one column "freq".
    """
    q = """
    with previous_highest_bids as (
    select
     b2.itemId
     ,b2.bidAmount as now_high_bid
     ,max(b1.bidAmount) as pre_high_bid
     ,i.bidIncrement
    from bids b2
    join bids b1 on b2.itemId = b1.itemId and b1.bidAmount < b2.bidAmount
    join items i on b2.itemId = i.itemId
    where i.isBuyNowUsed = 0
    group by b2.itemId, b2.bidAmount, i.bidIncrement
    )
    select
     sum(case when now_high_bid = pre_high_bid + bidIncrement then 1 else 0 end) * 1.0 / count(now_high_bid) as freq
    from previous_highest_bids;
    """
    return q

q3 = min_increment_freq()

print(auctions.query(q3))


## Exercise 4
def win_perc_by_timestamp() -> str:
    """
    Some docstrings.
    """
    q = """
    with auctiontime as (
        select itemid, min(bidTime) AS startime, max(bidTime) as endtime,
        from bids
    )
    """

    return q



