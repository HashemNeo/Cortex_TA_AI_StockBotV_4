from plotly import graph_objs as go
from datetime import date
import yfinance as yf
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tempfile
import io
plt.style.use('fivethirtyeight')

#Main part  
st.title("Cortex AI 😃")


#Retriving df2 from yfinance

start = '2005-01-01'
today = date.today().strftime("%Y-%m-%d")

string = "['Abu Dhabi Islamic Bank-Egypt (ADIB)', 'Abu Qir Fertilizers & Chemical Industries Co. (ABUK)', 'Acrow Misr (ACRO)', 'AJWA for Food Industries Co. Egypt (AJWA)', 'Al Arafa for Investments & Consultancies (AIVC)', 'Al Badr Investment & Development (BIDI)', 'Al Baraka Bank Egypt (SAUD)', 'Al Fanar Contracting Construction Trade Import & Export Co. (FNAR)', 'Al Khair River for Development Agriculture Investment & Environmental Services (KRDI)', 'Al Moasher for Programming & Information Dissemination (AMPI)', 'Al Tawfeek Leasing Co. (ATLC)', 'Alexandria Container & Cargo Handling Co. (ALCN)', 'Alexandria Flour Mills (AFMC)', 'Alexandria Mineral Oils Co. (AMOC)', 'Alexandria National Co. for Financial Investment (ANFI)', 'Alexandria New Medical Center Co. (AMES)', 'Alexandria Pharmaceuticals & Chemical Industries (AXPH)', 'Alexandria Spinning & Weaving (SPIN)', 'Amer Group Holding (AMER)', 'Arab Aluminium Co. SAE (ALUM)', 'Arab Ceramic Co.-Ceramica Remas (CERA)', 'Arab Co. for Asset Management & Development (ACAMD)', 'Arab Cotton Ginning (ACGC)', 'Arab Dairy Products Co. (ADPC)', 'Arab Developers Holding (ARAB)', 'Arab Drug Co. for Pharmaceuticals & Chemical Industries SAE (ADCI)', 'Arab Moltaka Investments Co. (AMIA)', 'Arab Polvara Spinning & Weaving Co. (APSW)', 'Arab Real Estate Investment (ALCO) (RREI)', 'Arab Valves Co. (ARVA)', 'Arabia Investments Holding (AIH)', 'Arabian Cement Co. (ARCC)', 'Arabian Food Industries Co. (DOMT)', 'Asek Co. for Mining (ASCM)', 'Aspire Capital Holding for Financial Investments (ASPI)', 'Atlas for Investment & Food Industry (AIFI)', 'B Investments Holding S.A.E. (BINV)', 'Barbary Investment Group (BIGP)', 'Belton Financial Holding (BTFH)', 'Cairo Educational Services S.A.E. (CAED)', 'Cairo for Investment & Real Estate Development SAE (CIRA)', 'Cairo Oils & Soap (COSG)', 'Cairo Pharmaceuticals & Chemicals Industries Co. (CPCI)', 'Cairo Poultry Co. (POUL)', 'Canal Shipping Agencies Co. (CSAG)', 'CI Capital Holding (CICH)', 'Citadel Capital SAE (CCAP)', 'Cleopatra Hospital (CLHO)', 'Commercial International Bank (Egypt) S.A.E. (COMI)', 'Contact Financial Holding (CNFN)', 'Credit Agricole Egypt (CIEB)', 'Delta Construction & Rebuilding (DCRC)', 'Delta for Printing & Packaging (DTPP)', 'Delta Insurance Co. (DEIN)', 'Delta Sugar Co. (SUGR)', 'Development & Engineering Consultants (DAPH)', 'Dice Sports & Casual Wear S.A.E. (DSCW)', 'East Delta Flour Mills (EDFM)', 'Eastern Co. SAE (EAST)', 'Edita Food Industries S.A.E. (EFID)', 'E-Finance for Digital & Financial Investements SAE (EFIH)', 'Egypt Aluminium Co. (EGAL)', 'Egypt for Poultry (EPCO)', 'Egypt Kuwait Holding Co. S.A.E. (EKHO)', 'Egypt Kuwait Holding Co. S.A.E. (EKHOA)', 'Egyptian Arabian Co. for Securities Brokerage (EASB)', 'Egyptian Chemical Industries (EGCH)', 'Egyptian Financial & Industrial Co. (EFIC)', 'Egyptian Financial Group-Hermes Holding Co. (HRHO)', 'Egyptian for Developing Building Materials (EDBM)', 'Egyptian for Tourism Resorts (EGTS)', 'Egyptian Gulf Bank (EGBE)', 'Egyptian International Pharmaceutical Industrial Co. (PHAR)', 'Egyptian Iron & Steel Co. (IRON)', 'Egyptian Media Production City Co. (MPRC)', 'Egyptian Modern Education Systems (MOED)', 'Egyptian Real Estate Group (AREH)', 'Egyptian Satellite Co. (EGSA)', 'Egyptian Transport & Commercial Services Co. SAE (ETRS)', 'Egyptians for Investment & Urban Development (EIUD)', 'Egyptians Housing Development & Reconstruction (EHDR)', 'El Ahli Investment & Development (AFDI)', 'El Ahram Co. for Printing & Packing (EPPK)', 'El Arabia Engineering Industries (EEII)', 'El Arabia for Land Reclamation (EALR)', 'El Ezz Dekheila Steel-Alexandria SAE (IRAX)', 'El Ezz Porcelain & Ceramic (Gemma) (ECAP)', 'El Kahera El Watania Investment (KWIN)', 'El Kahera Housing (ELKA)', 'El Nasr Clothes & Textiles (Kabo) (KABO)', 'El Nasr Co. for Civil Works (NCCW)', 'El Nasr for Manufacturing Agricultural Crops (ELNA)', 'El Obour Real Estate Investment (OBRI)', 'El Orouba Securities Brokerage (EOSB)', 'El Saeed Contracting & Real Estate Co. (UEGC)', 'El Shams Housing & Urbanization S.A.E. (ELSH)', 'El Wadi for International & Investment Development (ELWA)', 'Electro Cable Egypt Co. (ELEC)', 'Elsewedy Electric (SWDY)', 'Emaar Misr for Development SAE (EMFD)', 'Export Development Bank of Egypt (EXPA)', 'Extracted Oils & Derivatives Co. (ZEOT)', 'Ezz Steel Co. S.A.E. (ESRS)', 'Faisal Islamic Bank of Egypt (FAIT)', 'Faisal Islamic Bank of Egypt USD (FAITA)', 'Fawry for Banking Technology & Electronic Payment (FWRY)', 'First Investment & Real Estate Development Co. (FIRE)', 'Gadwa for Industrial Development (GDWA)', 'GB Auto S.A.E. (AUTO)', 'General Co. for Ceramics & Porcelain Products (PRCL)', 'General Co. for Land Reclamation Development & Reconstruction (AALR)', 'General Silos & Storage (GSSC)', 'Gharbia Islamic Housing Development (GIHD)', 'Giza General Contracting & Real Estate Investment (GGCC)', 'GlaxoSmithKline S.A.E. (BIOC)', 'Golden Coast Co. (GOCO)', 'Golden Textiles & Clothes Wool (GTWL)', 'Grand Investment Capital (GRCA)', 'Gulf Canadian Real Estate Investment Co. (CCRS)', 'Heliopolis Co. for Housing & Development (HELI)', 'Holding Co. for Financial Investment Lakah Group (HCFI)', 'Housing & Development Bank (HDBK)', 'Ibnsina Pharma (ISPH)', 'Industrial Engineering Co. for Construction & Development (ICON) (ENGC)', 'Integrated Diagnostics Holdings PLC (IDHC)', 'International Agricultural Products (IFAP)', 'International Business Corp. for Trading & Agencies (IBCT)', 'International Co. for Fertilizers & Chemicals (ICFC)', 'International Co. for Investment & Development (ICID)', 'International Co. for Leasing SAE (ICLE)', 'International Co. for Medical Industries (ICMI)', 'Iron & Steel for Mines & Quarries (ISMQ)', 'Ismailia Development & Real Estate Co. (IDRE)', 'Ismailia Misr Poultry Co. (ISMA)', 'Ismailia National Food Industries (INFI)', 'Juhayna Food Industries (JUFO)', 'Kafr El Zayat Pesticides & Chemicals (KZPC)', 'Lecico Egypt S.A.E. (LCSW)', 'Macro Group Pharmaceutical SAE (MCRO)', 'Madinet Nasr Housing & Development Co. (MNHD)', 'Mansourah Poultry (MPCO)', 'Maridive & Oil Services S.A.E. (MOIL)', 'Marsa Marsa Alam for Tourism Development (MMAT)', 'Marseille Almasreia Alkhalegeya For Holding Investment (MAAL)', 'MB for Engineering & Contracting (MBEN)', 'Medical Packaging Co. (MEPA)', 'Memphis Pharmaceutical & Chemical Industries (MPCI)', 'Mena Touristic & Real Estate Investments (MENA)', 'Middle & West Delta Flour Mills (WCDF)', 'Middle Egypt Flour Mills (CEFM)', 'Minapharm Pharmaceuticals (MIPH)', 'Misr Beni Suef Cement Co. (MBSC)', 'Misr Cement Co. Qena (MCQE)', 'Misr Chemical Industries Co. (MICH)', 'Misr Duty Free Shops (MFSC)', 'Misr Fertilizers Production Co. (MFPC)', 'Misr Hotels Co. (MHOT)', 'Misr Kuwait Investment & Trading Co. (MKIT)', 'Misr National Steel Ataqa (ATQA)', 'Misr Oils & Soap Co. (MOSC)', 'MM Group Industrial & International Trade (In Kind) (MTIE)', 'Mohandes Insurance (MOIN)', 'Naeem Holding Co. (NAHO)', 'National Housing for Professional Syndicates (NHPS)', 'National Real Estate Bank for Development (NRPD)', 'Natural Gas & Mining Project (Egypt Gas) (EGAS)', 'Nile Co. for Pharmaceutical & Chemical Industries (NIPH)', 'North Cairo Mills Co. (MILS)', 'Northern Upper Egypt Development & Agricultural Production Co. (NEDA)', 'Nozha International Hospital (NINH)', 'Obourland for Food Industries (OLFI)', 'October Pharma (OCPH)', 'Odin Investments (ODIN)', 'Orascom Development Egypt (ORHD)', 'Orascom Financial Holding (OFH)', 'Orascom Investment Holding SAE (OIH)', 'Oriental Weavers Group (ORWE)', 'Osool ESB Securities Brokerage (EBSC)', 'Paints & Chemical Industries Co. (PACH)', 'Palm Hills Development Co. S.A.E. (PHDC)', 'Pioneers Properties for Urban Development (PRDC)', 'Prime Holding (PRMH)', 'Pyramisa Hotels & Touristic Villages (PHTV)', 'Qatar National Bank Alahly (QNBA)', 'Rakta Paper Manufacturing (RAKT)', 'Raya Contact Center Co. (RACC)', 'Raya Holding for Financial Investments (RAYA)', 'Reacap Financial Investments (REAC)', 'REKAZ Financial Holding (RKAZ)', 'Remco for Touristic Villages Construction (RTVC)', 'Rowad Tourism (Al Rowad) (ROTO)', 'Rubex International for Plastic & Acrylic Manufacturing (RUBX)', 'Sabaa International Co. for Pharmaceutical & Chemical (SIPC)', 'Samad Misr-EGYFERT (SMFR)', 'Saudi Egyptian Investment & Finance (SEIG)', 'Sharkia National Food (SNFC)', 'Sharm Dreams Co. for Tourism Investment (SDTI)', 'Sidi Kerir Petrochemicals Co. (SKPC)', 'Sinai Cement Co. (SCEM)', 'Sixth of October Development & Investment Co. (OCDI)', 'Societe Arabe Internationale de Banque (SAIB)', 'South Cairo & Giza Mills & Bakeries Co. (SCFM)', 'South Valley Cement (SVCE)', 'Speed Medical SAE (SPMD)', 'Suez Canal Bank (CANA)', 'Suez Canal Co. for Technology Settling (SCTS)', 'Taaleem Management Services (TALM)', 'Talaat Mostafa Group Holding (TMGH)', 'Tanmiya for Real Estate Investment (TANM)', 'Telecom Egypt S.A.E. (ETEL)', 'Tenth of Ramadan Pharmaceutical Industries & Diagnostic (RMDA)', 'Thiqah for Business Administration & Development (TRST)', 'TransOceans Tours (TRTO)', 'United Arab Shipping Co. (UASG)', 'United Housing & Development (UNIT)', 'Universal for Paper & Packaging Materials (UNIP)', 'Upper Egypt Flour Mills (UEFM)', 'Utopia (UTOP)', 'VertiKa for Industry & Trade (VERT)', 'Wadi Kom Ombo Land Reclamation (WKOL)', 'Zahraa Maadi Investment & Development (ZMID)', 'Minapharm Pharmaceuticals (MIPH)', 'Misr Beni Suef Cement Co. (MBSC)', 'Misr Cement Co. Qena (MCQE)', 'Misr Chemical Industries Co. (MICH)', 'Misr Duty Free Shops (MFSC)', 'Misr Fertilizers Production Co. (MFPC)', 'Misr Hotels Co. (MHOT)', 'Misr Kuwait Investment & Trading Co. (MKIT)', 'Misr National Steel Ataqa (ATQA)', 'Misr Oils & Soap Co. (MOSC)', 'MM Group Industrial & International Trade (In Kind) (MTIE)', 'Mohandes Insurance (MOIN)', 'Naeem Holding Co. (NAHO)', 'National Housing for Professional Syndicates (NHPS)', 'National Real Estate Bank for Development (NRPD)', 'Natural Gas & Mining Project (Egypt Gas) (EGAS)', 'Nile Co. for Pharmaceutical & Chemical Industries (NIPH)', 'North Cairo Mills Co. (MILS)', 'Northern Upper Egypt Development & Agricultural Production Co. (NEDA)', 'Nozha International Hospital (NINH)', 'Obourland for Food Industries (OLFI)', 'October Pharma (OCPH)', 'Odin Investments (ODIN)', 'Orascom Development Egypt (ORHD)', 'Orascom Financial Holding (OFH)', 'Orascom Investment Holding SAE (OIH)', 'Oriental Weavers Group (ORWE)', 'Osool ESB Securities Brokerage (EBSC)', 'Paints & Chemical Industries Co. (PACH)', 'Palm Hills Development Co. S.A.E. (PHDC)', 'Pioneers Properties for Urban Development (PRDC)', 'Prime Holding (PRMH)', 'Pyramisa Hotels & Touristic Villages (PHTV)', 'Qatar National Bank Alahly (QNBA)', 'Rakta Paper Manufacturing (RAKT)', 'Raya Contact Center Co. (RACC)', 'Raya Holding for Financial Investments (RAYA)', 'Reacap Financial Investments (REAC)', 'REKAZ Financial Holding (RKAZ)', 'Remco for Touristic Villages Construction (RTVC)', 'Rowad Tourism (Al Rowad) (ROTO)', 'Rubex International for Plastic & Acrylic Manufacturing (RUBX)', 'Sabaa International Co. for Pharmaceutical & Chemical (SIPC)', 'Samad Misr-EGYFERT (SMFR)', 'Saudi Egyptian Investment & Finance (SEIG)', 'Sharkia National Food (SNFC)', 'Sharm Dreams Co. for Tourism Investment (SDTI)', 'Sidi Kerir Petrochemicals Co. (SKPC)', 'Sinai Cement Co. (SCEM)', 'Sixth of October Development & Investment Co. (OCDI)', 'Societe Arabe Internationale de Banque (SAIB)', 'South Cairo & Giza Mills & Bakeries Co. (SCFM)', 'South Valley Cement (SVCE)', 'Speed Medical SAE (SPMD)', 'Suez Canal Bank (CANA)', 'Suez Canal Co. for Technology Settling (SCTS)', 'Taaleem Management Services (TALM)', 'Talaat Mostafa Group Holding (TMGH)', 'Tanmiya for Real Estate Investment (TANM)', 'Telecom Egypt S.A.E. (ETEL)', 'Tenth of Ramadan Pharmaceutical Industries & Diagnostic (RMDA)', 'Thiqah for Business Administration & Development (TRST)', 'TransOceans Tours (TRTO)', 'United Arab Shipping Co. (UASG)', 'United Housing & Development (UNIT)', 'Universal for Paper & Packaging Materials (UNIP)', 'Upper Egypt Flour Mills (UEFM)', 'Utopia (UTOP)', 'VertiKa for Industry & Trade (VERT)', 'Wadi Kom Ombo Land Reclamation (WKOL)', 'Zahraa Maadi Investment & Development (ZMID)']"


# Split the string into a list based on the comma separator
stocks = string.split(",")

#Editing the list of stocks

stocks[0] = stocks[0][1:]
stocks = [item[1:-1] for item in stocks]
stocks = [item.replace("'", "") for item in stocks]

# Create a list of dictionaries with name and symbol keys
stock_list = []
for stock in stocks:
    stock_info = stock.strip().split("(")
    stock_list.append({"name": stock_info[0].strip(), "symbol": stock_info[1].strip().replace(")", "")})

df = pd.DataFrame(stock_list)
st.write(df)


stocks = [item.replace("'", "") for item in stocks]





st.header('Stock Selection')
# tic = "CCAP"
#stk = ["CCAP","AMPI","ACRO","ATLC","ALCN","AFMC","AMES","AMER","ALUM","ALCO","AIH","ARCC","ASPI","CNFN","SUGR","EAST","EASB","PHAR","IRON","ELEC","FIRE","GSSC","BIOC","GOCO","ICMI","INFI","MCRO","MOIL","MMAT","MENA","MBSC","OFH","OIH","EBSC","REAC","SIPC","SMFR","SPMD","TRST","UNIT","VERT","MBSC","EBSC","REAC","RAYA","SIPC","SMFR","TRST"]

#ticker = st.selectbox('Choose your stock symbol', stk)






df2 = st.file_uploader("Choose a CSV file", type="csv")

if df2 is not None:
    # Save the uploaded file to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(df2.read())

    # Read the CSV file
    #df2 = pd.read_csv(temp_file.name)
    #df2 = pd.read_csv(io.StringIO(temp_file.name.read().decode("utf-8")))
    df2 = pd.read_csv(temp_file.name)
    df2.set_index('Date', inplace=True)

st.header('Values Table')
st.dataframe(df2)
st.header('Closing Price Chart')
fig = st.line_chart(df2['Close'])


# Fibonacci Retracement

st.header('Fibonacci Retracement')
# Calculate the highest and lowest points to use as anchors for the Fibonacci retracement
high = df2['High'].max()
low = df2['Low'].min()

# Define the levels of the Fibonacci retracement
levels = [0, 0.236, 0.382, 0.5, 0.618, 1]

# Calculate the retracement levels
retracement_levels = []
for level in levels:
    retracement_levels.append(low + (high - low) * level)

# Create a dictionary mapping each level to its color
level_colors = {
    0: 'red',
    0.236: 'green',
    0.382: 'blue',
    0.5: 'yellow',
    0.618: 'violet'
}

# Plot the df2 and add the retracement levels as horizontal lines
fig = px.line(df2, x=df2.index, y='Close')
for level, color in level_colors.items():
    fig.add_shape(
        type='line',
        x0=df2.index[0],
        x1=df2.index[-1],
        y0=retracement_levels[levels.index(level)],
        y1=retracement_levels[levels.index(level)],
        line=dict(
            color=color,
            width=2,
            dash='dash'
        )
    )

st.plotly_chart(fig)


# 2.AROON CALCULATION
st.header('The Aroon calculation requires the tracking of the high and low prices, typically over 25 periods.')

# Calculate the Aroon Indicator
df2["Aroon Up"] = df2["Close"].rolling(25).apply(lambda x: (np.argmax(x) / 25) * 100)
df2["Aroon Down"] = df2["Close"].rolling(25).apply(lambda x: (np.argmin(x) / 25) * 100)

# Plot the Aroon Indicator
st.header('Aroon Indicator')
st.line_chart(df2["Aroon Up"])
st.line_chart(df2["Aroon Down"])


# 4. Average True Range (ATR)
st.header('Average True Range (ATR) - is a volatility indicator that helps identify potential breakouts or trend changes. (14 periods)')
# Calculate the ATR
df2["H-L"] = df2["High"] - df2["Low"]
df2["H-PC"] = abs(df2["High"] - df2["Close"].shift(1))
df2["L-PC"] = abs(df2["Low"] - df2["Close"].shift(1))
df2["TR"] = df2[["H-L", "H-PC", "L-PC"]].max(axis=1)
df2["ATR"] = df2["TR"].rolling(14).mean()

# Plot the ATR
st.line_chart(df2["ATR"])


# 5.Moving Average Convergence Divergence

st.header('Moving Average Convergence Divergence (MACD) - is a trend-following momentum indicator that helps identify potential trend changes.')
# Calculate the MACD
df2["26-day EMA"] = df2["Close"].ewm(span=26).mean()
df2["12-day EMA"] = df2["Close"].ewm(span=12).mean()
df2["MACD"] = df2["12-day EMA"] - df2["26-day EMA"]
df2["Signal"] = df2["MACD"].ewm(span=9).mean()

# Plot the MACD
st.text('MACD Chart')
st.line_chart(df2["MACD"])
st.text('Signal Chart')
st.line_chart(df2["Signal"])

# 6. Relative Strength Index
st.header('Relative Strength Index (RSI) - is a momentum indicator that helps identify overbought and oversold conditions.')

# Calculate the RSI
df2["change"] = df2["Close"] - df2["Close"].shift(1)
df2["gain"] = df2["change"].where(df2["change"] > 0, 0)
df2["loss"] = -df2["change"].where(df2["change"] < 0, 0)
df2["avg_gain"] = df2["gain"].rolling(14).mean()
df2["avg_loss"] = df2["loss"].rolling(14).mean()
df2["rs"] = df2["avg_gain"] / df2["avg_loss"]
df2["RSI"] = 100 - (100 / (1 + df2["rs"]))

# Plot the RSI
st.line_chart(df2["RSI"])


#7. Stochastic Oscillator 
st.header('Stochastic Oscillator - is a momentum indicator that helps identify overbought and oversold conditions.')

# Calculate the Stochastic Oscillator
df2["%K"] = 100 * ((df2["Close"] - df2["Low"].rolling(14).min()) / (df2["High"].rolling(14).max() - df2["Low"].rolling(14).min()))
df2["%D"] = df2["%K"].rolling(3).mean()

# Plot the Stochastic Oscillator
st.line_chart(df2["%K"])
st.line_chart(df2["%D"])


# 8. Rate of Change (ROC)
st.header('Rate of Change (ROC) - is a momentum indicator that helps identify potential trend changes by measuring the percent change in price over a period of time.')
# Calculate the Rate of Change
df2["ROC"] = df2["Close"].pct_change(periods=10) * 100

# Plot the Rate of Change
st.text('n = 10 periods "short term investing"')
st.line_chart(df2["ROC"])

df2["ROC"] = df2["Close"].pct_change(periods=200) * 100

# Plot the Rate of Change
st.text('n = 200 periods "long term investing"')
st.line_chart(df2["ROC"])


# 9. William %R
st.header('William %R - is a momentum indicator that helps identify overbought and oversold conditions. "period = 14 days"') 
# Calculate the William %R
df2["William %R"] = 100 - (100 / (1 + (df2["High"].rolling(14).max() / df2["Close"])))

# Plot the William %R
st.line_chart(df2["William %R"])


# 10. Ichimoku Cloud
st.header('Ichimoku Cloud - is a trend following indicator that helps identify support and resistance levels, as well as potential trend changes.')

# Calculate the Ichimoku Cloud
df2["Tenkan-sen"] = (df2["High"] + df2["Low"]) / 2
df2["Tenkan-sen"] = df2["Tenkan-sen"].rolling(9).mean()

df2["Kijun-sen"] = (df2["High"] + df2["Low"]) / 2
df2["Kijun-sen"] = df2["Kijun-sen"].rolling(26).mean()

df2["Senkou A"] = (df2["Tenkan-sen"] + df2["Kijun-sen"]) / 2
df2["Senkou A"] = df2["Senkou A"].shift(26)

df2["Senkou B"] = (df2["High"].rolling(52).max() + df2["Low"].rolling(52).min()) / 2
df2["Senkou B"] = df2["Senkou B"].shift(26)

df2["Chikou Span"] = df2["Close"].shift(-26)

# Plot the Ichimoku Cloud
st.line_chart(df2["Tenkan-sen"])
st.line_chart(df2["Kijun-sen"])
st.line_chart(df2["Senkou A"])
st.line_chart(df2["Senkou B"])
st.line_chart(df2["Chikou Span"])

# 11. Know Sure Thing (KST)
st.header("Know Sure Thing (KST) - is a momentum indicator that calculates the rate of change of multiple smoothed rates of change.")


# Calculate the Rate of Change
df2["ROC"] = df2["Close"].pct_change(periods=1) * 100

# Calculate the smoothed Rate of Change
df2["ROC_10"] = df2["ROC"].rolling(10).mean()
df2["ROC_30"] = df2["ROC"].rolling(30).mean()
df2["ROC_90"] = df2["ROC"].rolling(90).mean()
df2["ROC_360"] = df2["ROC"].rolling(360).mean()

# Calculate the KST
df2["KST"] = df2["ROC_10"] + df2["ROC_30"] * 2 + df2["ROC_90"] * 3 + df2["ROC_360"] * 4

# Plot the KST
st.line_chart(df2["KST"])



# 12. Parabolic SAR
st.header('Parabolic SAR - is a trend-following indicator that calculates the point at which a trend is likely to reverse.')

# Initialize the Parabolic SAR values
sar = df2.iloc[0]["Close"]
af = 0.02
ep = sar
sar_list = [sar]

# Loop through the stock df2 and calculate the Parabolic SAR
for i in range(1, len(df2)):
    if i == 1:
        if df2.iloc[i]["Close"] > df2.iloc[i-1]["Close"]:
            trend = "up"
        else:
            trend = "down"
    else:
        if trend == "up":
            if df2.iloc[i]["Close"] > df2.iloc[i-1]["Close"]:
                af = min(af + 0.02, 0.2)
                ep = max(ep, df2.iloc[i]["Close"])
                sar = sar + af * (ep - sar)
            else:
                trend = "down"
                af = 0.02
                sar = ep
                ep = df2.iloc[i]["Close"]
        else:
            if df2.iloc[i]["Close"] < df2.iloc[i-1]["Close"]:
                af = min(af + 0.02, 0.2)
                ep = min(ep, df2.iloc[i]["Close"])
                sar = sar + af * (ep - sar)
            else:
                trend = "up"
                af = 0.02
                sar = ep
                ep = df2.iloc[i]["Close"]
    sar_list.append(sar)

# Add the Parabolic SAR values to the stock df2 data
df2["Parabolic SAR"] = sar_list

# Plot the Parabolic SAR
st.line_chart(df2["Parabolic SAR"])


# 12. KST Oscillator
st.header('KST Oscillator - is a momentum indicator that calculates the rate of change of multiple smoothed rates of change.')

# Calculate the rate of change
df2["ROC"] = df2["Close"].pct_change(periods=1) * 100

# Calculate the smoothed rate of change
df2["ROC_10"] = df2["ROC"].rolling(10).mean()
df2["ROC_30"] = df2["ROC"].rolling(30).mean()
df2["ROC_60"] = df2["ROC"].rolling(60).mean()
df2["ROC_120"] = df2["ROC"].rolling(120).mean()

# Calculate the KST Oscillator
df2["KST"] = df2["ROC_10"] + df2["ROC_30"] * 2 + df2["ROC_60"] * 3 + df2["ROC_120"] * 4

# Plot the KST Oscillator
st.line_chart(df2["KST"])


# 13. Bollinger Band Width (BBW)
st.header('Bollinger Band Width (BBW) - is a volatility indicator that measures the distance between the upper and lower Bollinger Bands.')


# Calculate the moving average and standard deviation
df2["MA"] = df2["Close"].rolling(20).mean()
df2["STD"] = df2["Close"].rolling(20).std()

# Calculate the upper and lower Bollinger Bands
df2["Upper BB"] = df2["MA"] + (df2["STD"] * 2)
df2["Lower BB"] = df2["MA"] - (df2["STD"] * 2)

# Calculate the Bollinger Band Width
df2["BBW"] = df2["Upper BB"] - df2["Lower BB"]

# Plot the Bollinger Band Width
st.line_chart(df2["BBW"])

# 14. Commodity Channel Index (CCI)
st.header('Commodity Channel Index (CCI) - is a momentum indicator that compares the current closing price to the average closing price over a period of time.')

# Calculate the mean deviation
df2["Mean Deviation"] = df2["Close"].rolling(14).mean() - df2["Close"]

# Calculate the CCI
df2["CCI"] = df2["Mean Deviation"] / (0.015 * df2["Close"].rolling(14).std())

# Plot the CCI
st.line_chart(df2["CCI"])

# 15. Detrended Price Oscillator (DPO)
st.header('Detrended Price Oscillator (DPO) - is a momentum indicator that removes the trend of a market.')

# Calculate the DPO
df2["DPO"] = df2["Close"].rolling(21).mean() - df2["Close"].shift(int(21 / 2 + 1))

# Plot the DPO
st.line_chart(df2["DPO"])

#17. Elder-Ray Index (ERI)
st.header('Elder-Ray Index (ERI) - is a momentum indicator that calculates the difference between the highest high and the lowest low of a market.')


# Calculate the highest high and lowest low
df2["Highest High"] = df2["High"].rolling(14).max()
df2["Lowest Low"] = df2["Low"].rolling(14).min()

# Calculate the ERI
df2["ERI"] = df2["Highest High"] - df2["Lowest Low"]

# Plot the ERI
st.line_chart(df2["ERI"])

# 18. Vortex Indicator (VI)
st.header("Vortex Indicator (VI) - is a momentum indicator that calculates the difference between the sum of positive trend changes and the sum of negative trend changes.")

# Calculate the true range
df2["True Range"] = df2[["High", "Low", "Close"]].apply(lambda x: max(x) - min(x), axis=1)

# Calculate the positive and negative trend changes
df2["Positive Trend Change"] = df2["High"] - df2["High"].shift(1)
df2["Negative Trend Change"] = df2["Low"].shift(1) - df2["Low"]

# Calculate the VI
df2["VI"] = (df2["Positive Trend Change"].rolling(14).sum() / df2["True Range"].rolling(14).sum()) - (df2["Negative Trend Change"].rolling(14).sum() / df2["True Range"].rolling(14).sum())

# Plot the VI
st.line_chart(df2["VI"])

# 19. Fractal Adaptive Moving Average (FRAMA)

st.header('Fractal Adaptive Moving Average (FRAMA) - is a moving average that adapts to the volatility of a market.')


# Calculate the volatility
df2["Volatility"] = df2["Close"].diff().abs().rolling(2).mean()

# Calculate the fractal dimension
df2["Fractal Dimension"] = np.log(df2["Volatility"]) / np.log(df2["Close"].diff().abs().rolling(2).mean())

# Calculate the FRAMA
df2["FRAMA"] = df2["Close"].rolling(2).mean() + df2["Fractal Dimension"].rolling(10).mean() * (df2["Close"] - df2["Close"].rolling(2).mean())

# Plot the FRAMA
st.line_chart(df2["FRAMA"])

# 20. Awesome Oscillator (AO)
st.header('Awesome Oscillator (AO) - is a momentum indicator that calculates the difference between the 34-period and 5-period simple moving averages of the median price.')

df2["Median Price"] = (df2["High"] + df2["Low"]) / 2

# Calculate the 34-period and 5-period simple moving averages
df2["SMA_34"] = df2["Median Price"].rolling(34).mean()
df2["SMA_5"] = df2["Median Price"].rolling(5).mean()

# Calculate the AO
df2["AO"] = df2["SMA_34"] - df2["SMA_5"]

# Plot the AO
st.line_chart(df2["AO"])


#21. Chande Momentum Oscillator (CMO)
# st.header('Chande Momentum Oscillator (CMO) - is a momentum indicator that compares the difference between the sum of up closes and down closes to the sum of the absolute difference of up closes and down closes.')

# # Calculate the up and down closes
# df2["Up Closes"] = df2.apply(lambda x: x["Close"] if x["Close"] > x["Close"].shift(1) else 0, axis=1)
# df2["Down Closes"] = df2.apply(lambda x: x["Close"] if x["Close"] < x["Close"].shift(1) else 0, axis=1)

# # Calculate the CMO
# df2["CMO"] = (df2["Up Closes"].rolling(14).sum() - df2["Down Closes"].rolling(14).sum()) / (df2["Up Closes"].rolling(14).sum() + df2["Down Closes"].rolling(14).sum()) * 100

# # Plot the CMO
# st.line_chart(df2["CMO"])

#22. Kaufman's Adaptive Moving Average (KAMA)
st.header("Kaufman's Adaptive Moving Average (KAMA) - is a moving average that adapts to the volatility of a market.")

# Calculate the volatility
df2["Volatility"] = df2["Close"].diff().abs().rolling(2).mean()

# Calculate the efficiency ratio
df2["Efficiency Ratio"] = df2["Volatility"] / (df2["Close"].diff().abs().rolling(30).sum() / 30)

# Calculate the KAMA
df2["KAMA"] = df2["Close"].rolling(30).mean() + df2["Efficiency Ratio"].rolling(10).mean() * (df2["Close"] - df2["Close"].rolling(30).mean())

# Plot the KAMA
st.line_chart(df2["KAMA"])

#23. Coppock Curve
st.header("Coppock Curve - is a momentum indicator that uses the rate of change of a weighted moving average to identify potential trend changes.")


# Calculate the Coppock curve
df2["Coppock"] = (df2["Close"].rolling(14).sum() + df2["Close"].rolling(11).sum()) / 2

# Plot the Coppock curve
st.line_chart(df2["Coppock"])


