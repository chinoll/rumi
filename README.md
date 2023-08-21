# Rumi:Efficient Multi-Modal language Modeling
Rumi is an efficient Multi-Modal model that combines VIT, whisper, and LLaMa to construct an efficient Multi-Modal model.
# Data synthesis
Run dataset synthesis script
```
OPENAI_KEY=xxx python tools/caption_generate.py -i data/example.json -o example_caption.json
```
# TODO
- [x]  Release dataset synthesis script
- [ ]  Release Dataset
- [ ] Release Image Caption model
- [ ] Release multi-modal code and model