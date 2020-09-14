# Countries Quiz Game
Countries Quiz Game (CQG) is a console desktop application game about countries and continents, consists of 2 parts
### Practice mode
- which gives simple questions about countries and continents
- e.g. number of countries in a continent, where is a country, what is the capital of a country, number of languages in a country or continent, etc

### Learn mode

- **continents statistics**:
	- to know statistics about the continent 
	- e.g. number of countries, official languages, most spoken languages, etc
- **countries information** :
	- to know information about the country
	- e.g. capital, official languages, its continent, etc

### NOTES
- There is 2 directories: 
	- ``wrangling`` directory:
		- where data is [wrangled](https://en.wikipedia.org/wiki/Data_wrangling#:~:text=Data%20wrangling%2C%20sometimes%20referred%20to,downstream%20purposes%20such%20as%20analytics.)
		- gathering data directory, where data gathered from the site for each continent (6 directories)
		- Assess and Clean directory, where compile all continents data which gathered and assess it and clean it using pandas library
		- **Sub-Note** python code saved as .[ipynb](https://fileinfo.com/extension/ipynb)
	- ``console`` directory where the application and data (after wrangling it)
- The application data is gathered from 
[affairscloud](https://affairscloud.com/) site using python requests and beautiful soup 4 libraries and saved as '.csv' file for each continent using python Pandas library 
- No OOP
## Run
#### prerequisite
- [python3](https://www.python.org/downloads/) installed
- numpy 
- pandas
- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install numpy, pandas if it is not installed.

```bash
pip install numpy pandas
```
#### application
- open terminal in ``Countries Quiz Game/console`` directory then run the application
```bash
python main.py
```
## Screenshots

<img src="https://user-images.githubusercontent.com/39943970/93137577-ff522400-f6dd-11ea-9582-697b58d63474.png" width=910>

![p mode](https://user-images.githubusercontent.com/39943970/93137619-0e38d680-f6de-11ea-9f82-ea243b624f01.png)

![q3 ](https://user-images.githubusercontent.com/39943970/93137636-155fe480-f6de-11ea-9a91-eaae69e145e5.png)

![q5](https://user-images.githubusercontent.com/39943970/93137632-142eb780-f6de-11ea-821c-5e8de1938102.png)

![score](https://user-images.githubusercontent.com/39943970/93137652-1a249880-f6de-11ea-8595-eec4831931c4.png)

![answers](https://user-images.githubusercontent.com/39943970/93137663-214ba680-f6de-11ea-979c-808a8d897928.png)

![new mode](https://user-images.githubusercontent.com/39943970/93137673-26105a80-f6de-11ea-9ce4-81dc2baf93e7.png)

![learning mode](https://user-images.githubusercontent.com/39943970/93137689-29a3e180-f6de-11ea-98a0-9144d6a13257.png)

![contentes](https://user-images.githubusercontent.com/39943970/93137697-2d376880-f6de-11ea-85e4-56faf6ce1682.png)

![africa](https://user-images.githubusercontent.com/39943970/93137703-2f99c280-f6de-11ea-81
21-035076622b47.png)

![learning mode](https://user-images.githubusercontent.com/39943970/93137762-493b0a00-f6de-11ea-8aca-df2a573e55b4.png)

![enter country name](https://user-images.githubusercontent.com/39943970/93137793-55bf6280-f6de-11ea-94da-77db8277310a.png)

![egypt](https://user-images.githubusercontent.com/39943970/93137767-4b9d6400-f6de-11ea-904
e-26955e6f2c74.png)

![irap ](https://user-images.githubusercontent.com/39943970/93137810-5c4dda00-f6de-11ea-8ca0-04b9fecb4258.png)
