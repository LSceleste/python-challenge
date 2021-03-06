{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-10</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-10</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-10</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-10</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-10</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Profit/Losses\n",
       "0  Jan-10         867884\n",
       "1  Feb-10         984655\n",
       "2  Mar-10         322013\n",
       "3  Apr-10         -69417\n",
       "4  May-10         310503"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# File to Load (Remember to Change These)\n",
    "file_to_load = \"Resources/budget_data.csv\"\n",
    "\n",
    "# Read Purchasing File and store into Pandas data frame\n",
    "budget_data_pd = pd.read_csv(file_to_load)\n",
    "budget_data_pd.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total number of months is: 86\n"
     ]
    }
   ],
   "source": [
    "rowcount = budget_data_pd[\"Date\"].count()\n",
    "print(\"The total number of months is: \" + str(rowcount))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The net total Profit/Losses is: $38382578\n"
     ]
    }
   ],
   "source": [
    "nettotal = budget_data_pd[\"Profit/Losses\"].sum()\n",
    "nettotal\n",
    "print(\"The net total Profit/Losses is: $\" + str(nettotal))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>Previous</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-10</td>\n",
       "      <td>867884</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-10</td>\n",
       "      <td>984655</td>\n",
       "      <td>867884.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-10</td>\n",
       "      <td>322013</td>\n",
       "      <td>984655.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-10</td>\n",
       "      <td>-69417</td>\n",
       "      <td>322013.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-10</td>\n",
       "      <td>310503</td>\n",
       "      <td>-69417.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Profit/Losses  Previous\n",
       "0  Jan-10         867884       NaN\n",
       "1  Feb-10         984655  867884.0\n",
       "2  Mar-10         322013  984655.0\n",
       "3  Apr-10         -69417  322013.0\n",
       "4  May-10         310503  -69417.0"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "budget_data_pd[\"Previous\"] = budget_data_pd[\"Profit/Losses\"].shift(+1)\n",
    "budget_data_pd.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>Previous</th>\n",
       "      <th>Change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-10</td>\n",
       "      <td>867884</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-10</td>\n",
       "      <td>984655</td>\n",
       "      <td>867884.0</td>\n",
       "      <td>116771.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-10</td>\n",
       "      <td>322013</td>\n",
       "      <td>984655.0</td>\n",
       "      <td>-662642.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-10</td>\n",
       "      <td>-69417</td>\n",
       "      <td>322013.0</td>\n",
       "      <td>-391430.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-10</td>\n",
       "      <td>310503</td>\n",
       "      <td>-69417.0</td>\n",
       "      <td>379920.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Profit/Losses  Previous    Change\n",
       "0  Jan-10         867884       NaN       NaN\n",
       "1  Feb-10         984655  867884.0  116771.0\n",
       "2  Mar-10         322013  984655.0 -662642.0\n",
       "3  Apr-10         -69417  322013.0 -391430.0\n",
       "4  May-10         310503  -69417.0  379920.0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "budget_data_pd[\"Change\"] = budget_data_pd[\"Profit/Losses\"] - budget_data_pd[\"Previous\"]\n",
    "budget_data_pd.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>Previous</th>\n",
       "      <th>Change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>8.600000e+01</td>\n",
       "      <td>8.500000e+01</td>\n",
       "      <td>8.500000e+01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.463090e+05</td>\n",
       "      <td>4.436645e+05</td>\n",
       "      <td>-2.315118e+03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>5.363579e+05</td>\n",
       "      <td>5.389768e+05</td>\n",
       "      <td>7.634372e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-1.196225e+06</td>\n",
       "      <td>-1.196225e+06</td>\n",
       "      <td>-2.196167e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.821620e+05</td>\n",
       "      <td>1.586200e+05</td>\n",
       "      <td>-3.686650e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>5.703280e+05</td>\n",
       "      <td>5.698990e+05</td>\n",
       "      <td>7.724200e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.952262e+05</td>\n",
       "      <td>7.959140e+05</td>\n",
       "      <td>3.983190e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.170593e+06</td>\n",
       "      <td>1.170593e+06</td>\n",
       "      <td>1.926159e+06</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Profit/Losses      Previous        Change\n",
       "count   8.600000e+01  8.500000e+01  8.500000e+01\n",
       "mean    4.463090e+05  4.436645e+05 -2.315118e+03\n",
       "std     5.363579e+05  5.389768e+05  7.634372e+05\n",
       "min    -1.196225e+06 -1.196225e+06 -2.196167e+06\n",
       "25%     1.821620e+05  1.586200e+05 -3.686650e+05\n",
       "50%     5.703280e+05  5.698990e+05  7.724200e+04\n",
       "75%     7.952262e+05  7.959140e+05  3.983190e+05\n",
       "max     1.170593e+06  1.170593e+06  1.926159e+06"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "budget_data_pd.describe(include = np.number)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>Previous</th>\n",
       "      <th>Change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Feb-12</td>\n",
       "      <td>1170593</td>\n",
       "      <td>-755566.0</td>\n",
       "      <td>1926159.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>Dec-13</td>\n",
       "      <td>1150461</td>\n",
       "      <td>-687986.0</td>\n",
       "      <td>1838447.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>79</th>\n",
       "      <td>Aug-16</td>\n",
       "      <td>569899</td>\n",
       "      <td>-1163797.0</td>\n",
       "      <td>1733696.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>Sep-12</td>\n",
       "      <td>475062</td>\n",
       "      <td>-1022534.0</td>\n",
       "      <td>1497596.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Oct-13</td>\n",
       "      <td>268997</td>\n",
       "      <td>-1196225.0</td>\n",
       "      <td>1465222.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Date  Profit/Losses   Previous     Change\n",
       "25  Feb-12        1170593  -755566.0  1926159.0\n",
       "47  Dec-13        1150461  -687986.0  1838447.0\n",
       "79  Aug-16         569899 -1163797.0  1733696.0\n",
       "32  Sep-12         475062 -1022534.0  1497596.0\n",
       "45  Oct-13         268997 -1196225.0  1465222.0"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max_inc_profits = budget_data_pd.sort_values(\"Change\", ascending=False)\n",
    "max_inc_profits.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>Previous</th>\n",
       "      <th>Change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>Sep-13</td>\n",
       "      <td>-1196225</td>\n",
       "      <td>999942.0</td>\n",
       "      <td>-2196167.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>78</th>\n",
       "      <td>Jul-16</td>\n",
       "      <td>-1163797</td>\n",
       "      <td>712961.0</td>\n",
       "      <td>-1876758.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>73</th>\n",
       "      <td>Feb-16</td>\n",
       "      <td>-1100387</td>\n",
       "      <td>650000.0</td>\n",
       "      <td>-1750387.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Aug-12</td>\n",
       "      <td>-1022534</td>\n",
       "      <td>506702.0</td>\n",
       "      <td>-1529236.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>63</th>\n",
       "      <td>Apr-15</td>\n",
       "      <td>-524626</td>\n",
       "      <td>687533.0</td>\n",
       "      <td>-1212159.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Date  Profit/Losses  Previous     Change\n",
       "44  Sep-13       -1196225  999942.0 -2196167.0\n",
       "78  Jul-16       -1163797  712961.0 -1876758.0\n",
       "73  Feb-16       -1100387  650000.0 -1750387.0\n",
       "31  Aug-12       -1022534  506702.0 -1529236.0\n",
       "63  Apr-15        -524626  687533.0 -1212159.0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max_dec_profits = budget_data_pd.sort_values(\"Change\")\n",
    "max_dec_profits.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FINANCIAL ANALYSIS\n",
      "Total Months: 86\n",
      "Total: $38,382,578\n",
      "Avarage Change: $-2,315.12\n",
      "Greatest Increase in Profits: Feb-2012 ($1,926,159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($2,196,167)\n"
     ]
    }
   ],
   "source": [
    "print(\"FINANCIAL ANALYSIS\")\n",
    "print(\"Total Months: 86\")\n",
    "print(\"Total: $38,382,578\")\n",
    "print(\"Avarage Change: $-2,315.12\")\n",
    "print(\"Greatest Increase in Profits: Feb-2012 ($1,926,159)\")\n",
    "print(\"Greatest Decrease in Profits: Sep-2013 ($2,196,167)\")\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
