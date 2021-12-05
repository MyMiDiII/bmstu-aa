package encryption

import (
	"strings"
	"time"

	"github.com/brianvoe/gofakeit"
)

type Cipher struct {
	wordsNum int

	Msg string

	flagMsg      bool
	flagReplace  bool
	flagVegenere bool

	startMsg time.Time
	endMsg   time.Time

	startReplace time.Time
	endReplace   time.Time

	startVegenere time.Time
	endVegenere   time.Time
}

func GenerateMsg(msg *Cipher) {
	msg.Msg = gofakeit.Sentence(msg.wordsNum)
	msg.Msg = strings.TrimRight(strings.ToLower(msg.Msg), ".")
}

func reverseWords(msg *Cipher) {

}
