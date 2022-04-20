#
#  [3차] 방금그곡
#  https://programmers.co.kr/learn/courses/30/lessons/17683
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/15.
#


from typing import OrderedDict


def solution(m, musicinfos):
    # 00:00시부터 정렬
    musicinfos = sorted(musicinfos)
    music_play = dict()
    m = m

    for musicinfo in musicinfos:
        start, end, name, sound = musicinfo.split(",")
        new_music_play_minutes = getMinutes(end)-getMinutes(start)
        m = m[:new_music_play_minutes]
        print(m)

        # 재생되지 않았을 때
        if new_music_play_minutes == 0:
            continue

        # 이미 재생된 음악일 때
        if name in music_play.keys():
            music_play[name].append(getSound(new_music_play_minutes, sound))
        else:
            music_play[name] = [getSound(new_music_play_minutes, sound)]

    # 플레이 시간이 긴 순서대로 정렬한다.
    music_play = OrderedDict(sorted(
        music_play.items(), key=lambda music: len(music[1]), reverse=True))

    print(music_play)

    # m이 재생된 적 있는지 확인한다.
    for name, sounds in music_play.items():
        for sound in sounds:
            for i in range(len(sound)):
                # m을 sound에서 찾았을 때
                if i+len(m)-1 < len(sound) and m == sound[i:i+len(m)]:

                    # m뒤에 있는 문자가 "#"인지 확인하기
                    # 예) m = "ABC", sound = "ABC#" or m = "ABC#", sound = "ABC##"
                    if i+len(m) < len(sound) and sound[i+len(m)] == "#":
                        continue
                    else:
                        return name

    return "(None)"


def getMinutes(time: str) -> int:
    hour, minutes = map(int, time.split(":"))
    return hour*60+minutes


def getSound(play_time: int, sound: str) -> str:
    sound_len = len(sound)
    if play_time < sound_len:
        return sound[:play_time]
    elif play_time <= sound_len:
        return sound
    else:
        played_sound = sound
        index = 0
        while len(played_sound) < play_time:
            played_sound += sound[index]
            index = index+1 if index < len(sound)-1 else 0
        return played_sound


m = "A#ABC"
musicinfos = ["12:00,12:01,HELLO,A#"]
print(solution(m, musicinfos))
