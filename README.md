# Air Quality Sensor: Raspberry Pi 3 + SDS011 PM Sensor

Based on https://www.hackster.io/mjrobot/sensing-the-air-quality-58a074#toc-mqtt-protocol-and-thingspeak-connection-10

Measurements are published to a free ThingSpeak channel. https://thingspeak.com/channels/1606352 .

### MATLAB charts
#### PM 2.5 [µg/m³] (avg. by hour)
```
readChannelID = [];
readAPIKey = [];
fieldID = 1;

C_VERY_LOW = [168, 255, 168] / 255;
C_LOW = [0, 255, 0] / 255;
C_MEDIUM = [255, 196, 0] / 255;
C_HIGH = [255, 68, 0] / 255;
C_VERY_HIGH = [179, 0, 83];

%% CAQI %%
L_VERY_LOW = 15;
L_LOW = 30;
L_MEDIUM = 55;
L_HIGH = 110;

%% Read Data %%

[data, time] = thingSpeakRead(readChannelID, 'Field', fieldID, 'NumPoints', 7200, 'ReadKey', readAPIKey);
tt = retime(timetable(time,data),'hourly','mean');

%% Visualize Data %%

b = bar(tt.time, tt.data);
xlabel('Date') 
ylabel('PM 2.5 [µg/m³]') 
b.FaceColor = 'flat';
for k = 1:length(tt.data)
    value = tt.data(k)
    color = C_VERY_HIGH;
    if value <= L_VERY_LOW
        color = C_VERY_LOW;
    elseif value <= L_LOW
        color = C_LOW;
    elseif value <= L_MEDIUM
        color = C_MEDIUM
    elseif value <= L_HIGH
        color = C_HIGH
    end
    b.CData(k,:) = color;
end
```

#### PM 10 [µg/m³] (avg. by hour)
```
readChannelID = [];
readAPIKey = [];
fieldID = 3;

C_VERY_LOW = [168, 255, 168] / 255;
C_LOW = [0, 255, 0] / 255;
C_MEDIUM = [255, 196, 0] / 255;
C_HIGH = [255, 68, 0] / 255;
C_VERY_HIGH = [179, 0, 83];

%% CAQI %%
L_VERY_LOW = 25;
L_LOW = 50;
L_MEDIUM = 90;
L_HIGH = 180;

%% Read Data %%

[data, time] = thingSpeakRead(readChannelID, 'Field', fieldID, 'NumPoints', 7200, 'ReadKey', readAPIKey);
tt = retime(timetable(time,data),'hourly','mean');

%% Visualize Data %%

b = bar(tt.time, tt.data);
xlabel('Date') 
ylabel('PM 10 [µg/m³]') 
b.FaceColor = 'flat';
for k = 1:length(tt.data)
    value = tt.data(k)
    color = C_VERY_HIGH;
    if value <= L_VERY_LOW
        color = C_VERY_LOW;
    elseif value <= L_LOW
        color = C_LOW;
    elseif value <= L_MEDIUM
        color = C_MEDIUM
    elseif value <= L_HIGH
        color = C_HIGH
    end
    b.CData(k,:) = color;
end
```
