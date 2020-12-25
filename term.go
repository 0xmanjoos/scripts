package main

import (
	"log"
	"github.com/buger/goterm"
	ui "github.com/gizak/termui/v3"
	"github.com/gizak/termui/v3/widgets"
)

func main() {
	if err := ui.Init(); err != nil {
		log.Fatalf("failed to initialize termui: %v", err)
	}
	defer ui.Close()

	p := widgets.NewParagraph()
	p.Text = "Hello World!"
    h := goterm.Height()
    w := goterm.Width()
	p.SetRect(0, 0, w, h)

	ui.Render(p)

	for e := range ui.PollEvents() {
		if e.Type == ui.KeyboardEvent {
			break
		}
	}
}
