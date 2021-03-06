# Read a string with spaces using for loop
for value in ch-ae-01.protonvpn.net.tcp ch-ar-01.protonvpn.net.tcp ch-ar-01.protonvpn.net.tcp ch-ar-01.protonvpn.net.tcp ch-at-01.protonvpn.net.tcp ch-au-01.protonvpn.net.tcp ch-be-01.protonvpn.net.tcp ch-ca-01.protonvpn.net.tcp ch-cy-01.protonvpn.net.tcp ch-cz-01.protonvpn.net.tcp ch-de-01.protonvpn.net.tcp ch-dk-01.protonvpn.net.tcp ch-ee-01.protonvpn.net.tcp ch-es-01.protonvpn.net.tcp ch-fi-01.protonvpn.net.tcp ch-fr-01.protonvpn.net.tcp ch-gr-01.protonvpn.net.tcp ch-hu-01.protonvpn.net.tcp ch-ie-01.protonvpn.net.tcp ch-il-01.protonvpn.net.tcp ch-in-01.protonvpn.net.tcp ch-it-01.protonvpn.net.tcp ch-jp-01.protonvpn.net.tcp ch-lt-01.protonvpn.net.tcp ch-lu-01.protonvpn.net.tcp ch-lv-01.protonvpn.net.tcp ch-md-01.protonvpn.net.tcp ch-mx-01.protonvpn.net.tcp ch-my-01.protonvpn.net.tcp ch-nl-01.protonvpn.net.tcp ch-no-01.protonvpn.net.tcp ch-nz-01.protonvpn.net.tcp ch-pl-01.protonvpn.net.tcp ch-pt-01.protonvpn.net.tcp ch-rs-01.protonvpn.net.tcp ch-sg-01.protonvpn.net.tcp ch-si-01.protonvpn.net.tcp ch-sk-01.protonvpn.net.tcp ch-tw-01.protonvpn.net.tcp ch-ua-01.protonvpn.net.tcp ch-uk-01.protonvpn.net.tcp ch-us-01.protonvpn.net.tcp is-au-01.protonvpn.net.tcp is-be-01.protonvpn.net.tcp is-br-01.protonvpn.net.tcp is-ca-01.protonvpn.net.tcp is-cl-01.protonvpn.net.tcp is-co-01.protonvpn.net.tcp is-cr-01.protonvpn.net.tcp is-de-01.protonvpn.net.tcp is-dk-01.protonvpn.net.tcp is-es-01.protonvpn.net.tcp is-fr-01.protonvpn.net.tcp is-ge-01a.protonvpn.net.tcp is-hk-01.protonvpn.net.tcp is-hu-01.protonvpn.net.tcp is-ie-01.protonvpn.net.tcp is-il-01.protonvpn.net.tcp is-it-01.protonvpn.net.tcp is-lu-01.protonvpn.net.tcp is-nl-01.protonvpn.net.tcp is-no-01.protonvpn.net.tcp is-pe-01.protonvpn.net.tcp is-pr-01.protonvpn.net.tcp is-ru-01.protonvpn.net.tcp is-th-01.protonvpn.net.tcp is-uk-01.protonvpn.net.tcp is-us-01.protonvpn.net.tcp is-za-01.protonvpn.net.tcp se-au-01.protonvpn.net.tcp se-bg-01.protonvpn.net.tcp se-br-01.protonvpn.net.tcp se-ca-01.protonvpn.net.tcp se-de-01.protonvpn.net.tcp se-ee-01.protonvpn.net.tcp se-eg-01.protonvpn.net.tcp se-es-01.protonvpn.net.tcp se-fi-01.protonvpn.net.tcp se-fi-01.protonvpn.net.tcp se-fr-01.protonvpn.net.tcp se-hk-01.protonvpn.net.tcp se-jp-01.protonvpn.net.tcp se-kh-01.protonvpn.net.tcp se-kr-01.protonvpn.net.tcp se-lt-01.protonvpn.net.tcp se-md-01.protonvpn.net.tcp se-nl-01.protonvpn.net.tcp se-no-01.protonvpn.net.tcp se-nz-01.protonvpn.net.tcp se-ph-01.protonvpn.net.tcp se-pt-01.protonvpn.net.tcp se-ro-01.protonvpn.net.tcp se-ru-01.protonvpn.net.tcp se-sg-01.protonvpn.net.tcp se-tr-01.protonvpn.net.tcp se-tw-01.protonvpn.net.tcp se-uk-01.protonvpn.net.tcp se-us-01.protonvpn.net.tcp

do
    echo $value
    osascript -e 'tell application "Tunnelblick"
            connect "'$value'"
            get state of first configuration where name = "'$value'"
            repeat until result = "CONNECTED"
                    delay 1
                    get state of first configuration where name = "'$value'"
            end repeat
    end tell'
    sleep 3600
    osascript -e 'tell application "Tunnelblick"
    disconnect all
    end tell'
    echo "DISCONNECT"
done
