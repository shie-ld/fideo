[![Contributors][contributors-shield]]
[![Forks][forks-shield]]
[![Stargazers][stars-shield]]
[![Issues][issues-shield]]
[![MIT License][license-shield]]



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project

[![Project Screen Shot][project-screenshot]](https://github.com/shie-ld/fideo/blob/main/src/ss.png)

Hey fellos, have you ever wondered that in this age of cloud, where you want to fetch anything at anytime from anywhere from you own personal cloud storage, you can do it for free, as of now, without bothering to spend a single penny from your pocket. 

This project is aimed at:
* Encoding any file - pdf, image, zip archive, anything to a video
* Uploading that video to YouTube, as it provides us free umlimited cloud storage of videos
* Downloading that video anywhere and decoding back it into our original file

So in short, we are going to exploit the unlimited free cloud storage of videos provided by YouTube as our cloud backup of files. This is gonna be an short and interesting project with documentation at every step to help you in understanding what program does, and if you wish, you can change it as you want so it does computing what you wish, not what is decided by me.

### Built With

* [Python3](https://www.python.org/)
* [Jupyter notebook](https://jupyter.org/)



<!-- GETTING STARTED -->
## Getting Started

Grab a python3 distribution and run the source code with the help of jupyter notebook. Both of these get set up if you install anaconda distribution on your system - recommended way to run the project.

### Prerequisites

* bitstring
* Pillow
* glob3
* path.py
* ffmpeg-python

After installing anaconda, run 
```sh
pip install -r requirements.txt
```
in your terminal to install all the required dependencies and modules. Else they get installed automatically if you run the ipython notebook.

### Installation

1. Clone the repo
```sh
git clone https://github.com/shie-ld/fideo.git
```
2. Install required modules
```sh
pip install -r requirements.txt
```
3. Run the ipython notebook in `src` folder

Don't forget to put in the filename you want to encode in `encode_file` function in the last of the notebook. Check current directory and viola, you have encoded the file to video.



<!-- USAGE EXAMPLES -->
## Usage
Encode `file.zip` to `OUTFILE.mp4`: 
```sh
encode_file('file.zip')
```
Decode `OUTFILE.mp4` to `OUT.zip`:
```sh
decode_file('OUTFILE.mp4', 'OUT.zip')
```
which should come out to be an exact copy of `file.zip`. You can verify that by comparing the two files.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Rudresh Dixit - 00rudreshdixit@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/shie-ld/fideo)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/shie-ld/fideo.svg?style=flat-square
[contributors-url]: https://github.com/shie-ld/fideo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shie-ld/fideo.svg?style=flat-square
[forks-url]: https://github.com/shie-ld/fideo/network/members
[stars-shield]: https://img.shields.io/github/stars/shei-ld/fideo?style=flat-square
[stars-url]: https://github.com/shie-ld/fideo/stargazers
[issues-shield]: https://img.shields.io/github/issues/shie-ld/fideo.svg?style=flat-square
[issues-url]: https://github.com/shie-ld/fideo/issues
[license-shield]: https://img.shields.io/github/license/shie-ld/fideo.svg?style=flat-square
[license-url]: https://github.com/shie-ld/fideo/blob/main/LICENSE
[product-screenshot]: images/screenshot.png
