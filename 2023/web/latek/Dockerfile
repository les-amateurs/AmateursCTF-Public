FROM sharelatex/sharelatex-base
# tried to use a chinese tex full image but eh bad
# ROM thomasweise/docker-texlive-full
# RUN sed -i 's/mirrors\.ustc\.edu\.cn/archive.ubuntu.com/g' /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive

# basic latex functions, thanks not overleaf
# from https://github.com/overleaf/overleaf/blob/main/server-ce/Dockerfile-base

# RUN tlmgr init-usertree
RUN tlmgr install --repository https://mirror.math.princeton.edu/pub/CTAN/systems/texlive/tlnet scheme-context bibtex hyperref csquotes bookmark times units underscore amsfonts amsmath anysize beamer booktabs breqn caption cite cmap crop ctable eso-pic euenc euler etoolbox extsizes fancybox fancyref fancyvrb filehook float fontspec fp index jknapltx koma-script latexbug l3experimental l3kernel l3packages lineno listings lwarp mathspec mathtools mdwtools memoir metalogo microtype ms ntgclass parskip pdfpages polyglossia powerdot psfrag rcs sansmath section seminar sepnum setspace subfig textcase thumbpdf translator typehtml ucharcat underscore unicode-math xcolor xkeyval xltxtra xunicode
#scheme-context amsmath tools metafont mfware bibtex lualatex-math l3build hyperref csquotes bookmark times units underscore amsfonts

RUN apt-get update && apt-get install -y python3 python3-pip gunicorn

RUN pip3 install flask nanoid
COPY flag.txt /

RUN adduser --home /app app

RUN tlmgr install --repository https://mirror.math.princeton.edu/pub/CTAN/systems/texlive/tlnet xpatch asymptote yhmath thmtools mdframed zref needspace

RUN chown -R app:app /app || echo Ouch chown fail
USER app
WORKDIR /app
COPY app/* /app/
COPY app/templates/* /app/templates/
COPY app/inputs/* /app/inputs/
RUN mkdir /app/documents

RUN rm -rf /var/lib/sharelatex /var/log/sharelatex
RUN userdel -r sharelatex

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:5000", "-n", "Latek Server"]
# ENTRYPOINT ["python3", "app.py"]