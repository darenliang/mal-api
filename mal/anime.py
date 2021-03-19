from typing import Optional, List, Dict

from mal import config, base
from mal.mal import _MAL


class Anime(_MAL):
    def __init__(self, mal_id: int, timeout: int = config.TIMEOUT, debug: bool = False):
        """
        Anime query by ID
        :param mal_id: MyAnimeList ID
        :param timeout: Timeout in seconds
        """
        super().__init__(mal_id, "anime", timeout, debug)

    def reload(self) -> None:
        """
        Reload anime query
        :return: None
        """
        self.__init__(self._mal_id)

    class _Character(object):
        def __init__(self,_name,_actor):
            self.name = _name
            self.actor = _actor
            #print(_name,_actor)

        def __str__(self):
            #print("_Char:",[self.name,self.actor])
            return self.name+':'+self.actor

        def __repr__(self):
            return "'"+self.name+':'+self.actor+"'"

    def _get_op_ed(self, option) -> List[str]:
        """
        Get list of OP or ED
        :param option: "op" or "ed"
        :return: List of OP or ED
        """
        themes = []
        if option == "op":
            data = self._page.find("div", {"class": "opnening"}).parent
        else:
            data = self._page.find("div", {"class": "ending"}).parent
        data = data.findChildren("span", {"class": "theme-song"})
        if data:
            if len(data) > 1:
                for theme in data:
                    themes.append(theme.text[4:])
            else:
                themes = [data[0].text]
        return themes

    def _get_characters(self) -> List[str]:
        """
        Get list of characters and voice actors
        :param option: 
        :return: List of Characters
        """
        characters = []
        data = self._page.find("div", {"class": "detail-characters-list clearfix"})
        chars = data.findChildren("tr")
        for i in range(len(chars)):
            if not i%2:
                _name = chars[i].find('h3', {"class": "h3_characters_voice_actors"} ).select('a')[0].text
            else:
                _actor = chars[i].select('a')[0].text
                characters.append(Anime._Character(_name,_actor))
            #chars = [ x.text for x in self._page.findAll('h3', {"class": "h3_characters_voice_actors"} )]
        return characters

    def _get_staff(self) -> List[str]:
        """
        Get list of staff
        :param option: 
        :return: List of staff
        """
        data = self._page.findAll("div", {"class": "detail-characters-list clearfix"})[1] #staff has the same class as the voice actors, so selecting second tag 
        data = data.findAll('td', {"class": "borderClass"} )[1::2] #since the pics are class 'ac borderClass' they are also selected, skipping them
        staff = [ x.select('a')[0].text for x in data ]
        return staff

    @property
    @base.property
    def episodes(self) -> Optional[int]:
        """
        Get episodes
        :return: Episodes count
        """
        try:
            self._episodes
        except AttributeError:
            self._episodes = self._get_span_text(self._border_spans, "Episodes:", int)
        return self._episodes

    @property
    @base.property
    def aired(self) -> Optional[str]:
        """
        Get aired
        :return: Aired status
        """
        try:
            self._aired
        except AttributeError:
            self._aired = self._get_span_text(self._border_spans, "Aired:", str)
        return self._aired

    @property
    @base.property
    def premiered(self) -> Optional[str]:
        """
        Get premiered
        :return: Premiered status
        """
        try:
            self._premiered
        except AttributeError:
            self._premiered = self._get_span_text(self._border_spans, "Premiered:", str)
        return self._premiered

    @property
    @base.property
    def broadcast(self) -> Optional[str]:
        """
        Get broadcast
        :return: Broadcast status
        """
        try:
            self._broadcast
        except AttributeError:
            self._broadcast = self._get_span_text(self._border_spans, "Broadcast:", str)
        return self._broadcast

    @property
    @base.property_list
    def producers(self) -> List[str]:
        """
        Get producers
        :return: List of producers
        """
        try:
            self._producers
        except AttributeError:
            self._producers = self._get_span_text(
                self._border_spans, "Producers:", list
            )
        return self._producers

    @property
    @base.property_list
    def licensors(self) -> List[str]:
        """
        Get licensors
        :return: List of licensors
        """
        try:
            self._licensors
        except AttributeError:
            self._licensors = self._get_span_text(
                self._border_spans, "Licensors:", list
            )
        return self._licensors

    @property
    @base.property_list
    def studios(self) -> List[str]:
        """
        Get studios
        :return: List of studios
        """
        try:
            self._studios
        except AttributeError:
            self._studios = self._get_span_text(self._border_spans, "Studios:", list)
        return self._studios

    @property
    @base.property
    def source(self) -> Optional[str]:
        """
        Get source
        :return: Source
        """
        try:
            self._source
        except AttributeError:
            self._source = self._get_span_text(self._border_spans, "Source:", str)
        return self._source

    @property
    @base.property
    def duration(self) -> Optional[str]:
        """
        Get duration
        :return: Duration string
        """
        try:
            self._duration
        except AttributeError:
            self._duration = self._get_span_text(self._border_spans, "Duration:", str)
        return self._duration

    @property
    @base.property
    def rating(self) -> Optional[str]:
        """
        Get age rating
        :return: Age rating
        """
        try:
            self._rating
        except AttributeError:
            self._rating = self._get_span_text(self._border_spans, "Rating:", str)
        return self._rating

    @property
    @base.property_dict
    def related_anime(self) -> Dict[str, List[str]]:
        """
        Get related anime
        :return: Dict of related anime
        """
        try:
            self._related_anime
        except AttributeError:
            self._related_anime = self._get_related()
        return self._related_anime

    @property
    @base.property_list
    def opening_themes(self) -> List[str]:
        """
        Get opening themes
        :return: List of opening themes
        """
        try:
            self._opening_themes
        except AttributeError:
            self._opening_themes = self._get_op_ed("op")
        return self._opening_themes

    @property
    @base.property_list
    def ending_themes(self) -> List[str]:
        """
        Get ending themes
        :return: List of ending themes
        """
        try:
            self._ending_themes
        except AttributeError:
            self._ending_themes = self._get_op_ed("ed")
        return self._ending_themes

    @property
    @base.property_list
    def characters(self) -> List[_Character]:
        """
        Get characters
        :return: List of characters
        """
        try:
            self._characters
        except AttributeError:
            self._characters = self._get_characters()
        return self._characters

    @property
    @base.property_list
    def staff(self) -> List[str]:
        """
        Get staff
        :return: List of staff
        """
        try:
            self._staff
        except AttributeError:
            self._staff = self._get_staff()
        return self._staff


    @property
    @base.property
    def synopsis(self) -> Optional[str]:
        """
        Get synopsis
        :return: Synopsis text
        """
        try:
            self._synopsis
        except AttributeError:
            self._synopsis = self._get_itemprop_value(
                self._page, "description", "p", str
            )
        return self._synopsis

    @property
    @base.property
    def background(self) -> Optional[str]:
        """
        Get background info
        :return: Background info
        """
        try:
            self._background
        except AttributeError:
            self._background = self._parse_background("div")
        return self._background
