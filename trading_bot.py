def bot_advice(data):
    # Example trading strategy based on multiple factors

    # Check if there's a recent Golden Cross
    if data['Golden Cross Dates'].any():
        # Check if the average volume is high
        if data['Average Volume'].iloc[-1] > 100000:
            # Check if the most recent Daily Return is positive
            if data['Daily Returns'].iloc[-1] > 0:
                # Check if the Cumulative Returns are positive
                if data['Cumulative Returns'].iloc[-1] > 0:
                    # Check if the SMA is above the EMA
                    if data['SMA'].iloc[-1] > data['EMA'].iloc[-1]:
                        # Check if the Close is above the SMA
                        if data['Close'].iloc[-1] > data['SMA'].iloc[-1]:
                            # Check if the Volume is increasing
                            if data['Volume'].iloc[-1] > data['Volume'].iloc[-2]:
                                advice = "Consider buying. Recent Golden Cross, high average daily volume, positive daily return, positive cumulative returns, SMA above EMA, Close above SMA, and increasing volume."
                            else:
                                advice = "Hold. Recent Golden Cross, high average daily volume, positive daily return, positive cumulative returns, SMA above EMA, Close above SMA, but volume is not increasing."
                        else:
                            advice = "Hold. Recent Golden Cross, high average daily volume, positive daily return, positive cumulative returns, SMA above EMA, but Close is not above SMA."
                    else:
                        advice = "Hold. Recent Golden Cross, high average daily volume, positive daily return, positive cumulative returns, but SMA is not above EMA."
                else:
                    advice = "Consider buying. Recent Golden Cross, high average daily volume, positive daily return, but be cautious about recent negative cumulative returns."
            else:
                advice = "Consider buying. Recent Golden Cross and high average daily volume, but be cautious about recent negative daily return."
        else:
            advice = "Hold. Recent Golden Cross, but average daily volume is not high enough for a strong buy signal."
    # Check if there's a recent Death Cross
    elif data['Death Cross Dates'].any():
        # Check if the average volume is high
        if data['Average Volume'].iloc[-1] > 100000:
            # Check if the most recent Daily Return is negative
            if data['Daily Returns'].iloc[-1] < 0:
                # Check if the Cumulative Returns are negative
                if data['Cumulative Returns'].iloc[-1] < 0:
                    # Check if the SMA is below the EMA
                    if data['SMA'].iloc[-1] < data['EMA'].iloc[-1]:
                        # Check if the Close is below the SMA
                        if data['Close'].iloc[-1] < data['SMA'].iloc[-1]:
                            # Check if the Volume is increasing
                            if data['Volume'].iloc[-1] > data['Volume'].iloc[-2]:
                                advice = "Consider selling. Recent Death Cross, high average daily volume, negative daily return, negative cumulative returns, SMA below EMA, Close below SMA, and increasing volume."
                            else:
                                advice = "Hold. Recent Death Cross, high average daily volume, negative daily return, negative cumulative returns, SMA below EMA, Close below SMA, but volume is not increasing."
                        else:
                            advice = "Hold. Recent Death Cross, high average daily volume, negative daily return, negative cumulative returns, SMA below EMA, but Close is not below SMA."
                    else:
                        advice = "Hold. Recent Death Cross, high average daily volume, negative daily return, negative cumulative returns, but SMA is not below EMA."
                else:
                    advice = "Consider selling. Recent Death Cross, high average daily volume, negative daily return, but be cautious about recent positive cumulative returns."
            else:
                advice = "Consider selling. Recent Death Cross and high average daily volume, but be cautious about recent positive daily return."
        else:
            advice = "Hold. Recent Death Cross, but average daily volume is not high enough for a strong sell signal."
    else:
        advice = "Hold. No specific trading signals based on the current analysis."

    return advice
