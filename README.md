# Rumi:Efficient Multi-Modal language Modeling
Rumi is an efficient Multi-Modal model that combines VIT, whisper, and LLaMa to construct an efficient Multi-Modal model.
# Data synthesis
Run dataset synthesis script
```bash
python tools/prepare.py -i https://pixiv.nl/78286152-2.png -o example.json
OPENAI_KEY=xxx python tools/caption_generate.py -i example.json -o caption.json
```
or
```bash
OPENAI_KEY=xxx python tools/caption_generate.py -i data/example.json -o caption.json
```

# TODO
- [x] Release dataset synthesis script
- [ ] Release Image Caption model
- [ ] Release Dataset
- [ ] Release multi-modal code and model