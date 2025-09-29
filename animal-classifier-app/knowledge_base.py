# In knowledge_base.py
# Note: Conservation statuses and population estimates are general and can change.

ANIMAL_INFO = {
    # --- MAMMALS ---
    "Antelope": {
        "title": "Swift Herbivore of Grasslands",
        "details": {
            "features": "- Slender, graceful build with long legs and curved horns.\n- Excellent runners, capable of high speeds and long leaps.",
            "population": "- Varies greatly by species. Some, like the Springbok, are numerous, while others, like the Saiga Antelope, are Critically Endangered.",
            "preservation": "- Protect grassland habitats from agriculture.\n- Combat poaching for horns and meat.\n- Establish wildlife corridors to connect fragmented populations."
        }
    },
    "Badger": {
        "title": "Burrowing Omnivore",
        "details": {
            "features": "- Stocky, powerful body with short legs and strong claws for digging.\n- Distinctive black and white striped face.",
            "population": "- Generally widespread and stable (Least Concern), but local populations can be threatened by habitat loss.",
            "preservation": "- Protect ancient woodlands and pastures where they build their setts (burrows).\n- Reduce road mortality through wildlife crossings."
        }
    },
    "Bat": {
        "title": "Nocturnal Flying Mammal & Pollinator",
        "details": {
            "features": "- The only mammals capable of true sustained flight.\n- Use echolocation to navigate and hunt insects in the dark.",
            "population": "- Over 1,400 species. Many are threatened due to habitat loss and disease (like white-nose syndrome).",
            "preservation": "- Protect natural caves and old-growth forests that serve as roosts.\n- Reduce pesticide use.\n- Install bat boxes to provide alternative habitats."
        }
    },
    "Bear": {
        "title": "Large Omnivorous Mammal",
        "details": {
            "features": "- Large, stocky body with a thick coat of fur.\n- Excellent sense of smell.\n- Plantigrade walkers (walk on the soles of their feet).",
            "population": "- Varies from abundant (American Black Bear) to Vulnerable (Polar Bear, ~25,000 remaining).",
            "preservation": "- Conserve large, connected wilderness areas.\n- Mitigate human-bear conflict through proper waste management and education.\n- Combat poaching."
        }
    },
    "Bison": {
        "title": "Large Bovine of North America & Europe",
        "details": {
            "features": "- Massive head and forequarters with a prominent shoulder hump.\n- Thick, shaggy coat.",
            "population": "- A conservation success, recovered from a few hundred to over 30,000 in conservation herds. Still Near Threatened.",
            "preservation": "- Restore and manage large prairie ecosystems.\n- Maintain genetic diversity between herds.\n- Support programs that reintroduce bison to native lands."
        }
    },
    "Boar": {
        "title": "Wild Pig & Hardy Omnivore",
        "details": {
            "features": "- Solidly built with a long, bristly coat and a straight tail.\n- Males (boars) have sharp tusks that grow continuously.",
            "population": "- Widespread and abundant (Least Concern). Often considered an invasive species in many parts of the world.",
            "preservation": "- Management focuses on population control to mitigate damage to crops and native ecosystems rather than preservation."
        }
    },
    "Cat": {
        "title": "Domestic Feline",
        "details": {
            "features": "- Small, carnivorous mammal with retractable claws.\n- Known for agility, balance, and keen senses of hearing and sight.",
            "population": "- Globally abundant as a domesticated animal.",
            "preservation": "- Focus is on managing feral populations to prevent their negative impact on native birds and small mammals through trap-neuter-return (TNR) programs."
        }
    },
    "Chimpanzee": {
        "title": "Intelligent Great Ape",
        "details": {
            "features": "- Our closest living relative, sharing ~98% of our DNA.\n- Highly social and known for complex tool use.",
            "population": "- Endangered, with populations having declined sharply due to habitat loss and poaching. Estimates range from 170,000 to 300,000.",
            "preservation": "- Protect rainforest habitats.\n- Enforce strict anti-poaching laws.\n- Support sanctuaries for orphaned chimpanzees and combat the illegal pet trade."
        }
    },
    "Cow": {
        "title": "Domesticated Bovine",
        "details": {
            "features": "- Large domesticated ungulate, raised for meat (beef) and milk (dairy).\n- Ruminant with a four-chambered stomach.",
            "population": "- Globally abundant, with over 1.5 billion head of cattle.",
            "preservation": "- Focus is on sustainable agriculture, managing environmental impact (methane), and preserving heritage breeds."
        }
    },
    "Coyote": {
        "title": "Adaptable North American Canid",
        "details": {
            "features": "- Smaller than a wolf, with a slender build, pointed ears, and a bushy tail.\n- Highly adaptable to various habitats, including urban areas.",
            "population": "- Abundant and expanding its range (Least Concern).",
            "preservation": "- Management focuses on coexistence and mitigating human-coyote conflict in urban and agricultural settings."
        }
    },
    "Deer": {
        "title": "Widespread Herbivorous Mammal",
        "details": {
            "features": "- Ruminant mammals, males (bucks/stags) grow and shed antlers annually.\n- Long, powerful legs for running and leaping.",
            "population": "- Most species are abundant (Least Concern), though some, like the Père David's deer, were once extinct in the wild.",
            "preservation": "- Preserve woodland and forest habitats.\n- Manage populations through regulated hunting to prevent overgrazing and vehicle collisions."
        }
    },
    "Dog": {
        "title": "Domesticated Canid",
        "details": {
            "features": "- The first domesticated animal, bred into hundreds of diverse breeds.\n- Highly social pack animal.",
            "population": "- Globally abundant, with an estimated 900 million individuals.",
            "preservation": "- Focus is on managing feral dog populations to control disease (rabies) and protect wildlife from predation. Preserve rare and ancient breeds."
        }
    },
    "Dolphin": {
        "title": "Intelligent Marine Mammal",
        "details": {
            "features": "- Sleek, streamlined body for efficient swimming.\n- Highly intelligent and social, using clicks and whistles to communicate.",
            "population": "- Many species are abundant, but some coastal populations and river dolphins (like the Amazon river dolphin) are Endangered.",
            "preservation": "- Reduce plastic pollution and chemical runoff in oceans.\n- Implement sustainable fishing practices to prevent bycatch.\n- Establish marine protected areas (MPAs)."
        }
    },
    "Donkey": {
        "title": "Domesticated Equid",
        "details": {
            "features": "- Known for long ears, a stocky build, and a loud bray.\n- Sure-footed and resilient, adapted to desert life.",
            "population": "- Abundant globally as a working animal. Wild ass species are Critically Endangered.",
            "preservation": "- Improve welfare for working donkeys.\n- Protect the critically endangered African wild ass, the ancestor of the domestic donkey."
        }
    },
    "Elephant": {
        "title": "Keystone Species & Ecosystem Engineer",
        "details": {
            "features": "- Largest land animal, characterized by its long trunk (proboscis), large ears, and tusks.\n- Highly intelligent with complex social structures.",
            "population": "- African species are Endangered, Asian species are Endangered. Populations are declining due to poaching and habitat loss.",
            "preservation": "- Enforce strict anti-poaching laws to stop the ivory trade.\n- Secure and manage large conservation areas and wildlife corridors.\n- Mitigate human-elephant conflict."
        }
    },
    "Fox": {
        "title": "Small, Cunning Canid",
        "details": {
            "features": "- Slender body, pointed snout, and a long, bushy tail (brush).\n- Known for its intelligence and adaptability.",
            "population": "- Most species, like the Red Fox, are widespread and abundant (Least Concern).",
            "preservation": "- Generally not a preservation focus. Management is aimed at controlling rabies and managing their impact on livestock and native fauna in places like Australia."
        }
    },
    "Goat": {
        "title": "Domesticated Caprine",
        "details": {
            "features": "- Hardy and agile ruminant, often with horns and a beard.\n- Known for their inquisitive nature.",
            "population": "- Abundant globally as livestock. Wild goat species (like the Iberian Ibex) can be Vulnerable.",
            "preservation": "- Control feral goat populations to protect native island ecosystems.\n- Conserve wild goat species and their rugged mountain habitats."
        }
    },
    "Gorilla": {
        "title": "Largest Living Primate",
        "details": {
            "features": "- Large, powerful build with a broad chest and muscular arms.\n- Gentle, herbivorous giants living in family groups.",
            "population": "- Critically Endangered. Both species (Eastern and Western) have low population numbers (e.g., ~1,000 Mountain Gorillas).",
            "preservation": "- Implement intensive anti-poaching patrols.\n- Support regulated ecotourism that funds conservation.\n- Protect their forest habitats from logging and agriculture."
        }
    },
    "Hamster": {
        "title": "Small Rodent",
        "details": {
            "features": "- Stout-bodied with large internal cheek pouches to carry food.\n- Short tail and small, furry ears.",
            "population": "- Common as pets, but the wild Syrian hamster is Vulnerable, and other wild species are also threatened.",
            "preservation": "- Protect their native grassland and agricultural habitats.\n- Conduct research on the status of threatened wild populations."
        }
    },
    "Hare": {
        "title": "Fast-Running Herbivore",
        "details": {
            "features": "- Larger than rabbits, with very long hind legs for running and long ears.\n- Nest in shallow depressions called 'forms' rather than burrows.",
            "population": "- Most species are abundant (Least Concern).",
            "preservation": "- Maintain open grassland and heathland habitats.\n- Manage agricultural practices to be more wildlife-friendly."
        }
    },
    "Hedgehog": {
        "title": "Spiny Nocturnal Mammal",
        "details": {
            "features": "- Covered in thousands of stiff spines (quills) which they use for defense by rolling into a ball.\n- Nocturnal insectivores.",
            "population": "- Declining rapidly in some regions like the UK (now Vulnerable there) due to habitat loss and fragmentation.",
            "preservation": "- Create 'hedgehog highways' (holes in fences) to connect gardens.\n- Maintain log piles and leafy areas for hibernation.\n- Reduce the use of slug pellets and other pesticides."
        }
    },
    "Hippopotamus": {
        "title": "Large, Semi-Aquatic Mammal",
        "details": {
            "features": "- Barrel-shaped torso, enormous mouth with large canine tusks.\n- Spends most of the day in water to keep cool.",
            "population": "- Vulnerable, with an estimated 115,000-130,000 remaining. Threatened by habitat loss and poaching for meat and ivory from their teeth.",
            "preservation": "- Protect and restore river and lake habitats.\n- Enforce anti-poaching laws.\n- Mitigate human-hippo conflict, as they can be dangerous."
        }
    },
    "Horse": {
        "title": "Domesticated Equid",
        "details": {
            "features": "- Large, strong mammal known for speed and endurance.\n- Has a 'fight or flight' response and lives in social herds.",
            "population": "- Abundant globally as a domesticated animal. The only truly wild horse, Przewalski's horse, is Endangered but recovering through reintroduction.",
            "preservation": "- Protect and manage feral horse populations (Mustangs, Brumbies).\n- Continue conservation breeding programs for Przewalski's horse."
        }
    },
    "Hyena": {
        "title": "Powerful Scavenger and Hunter",
        "details": {
            "features": "- Powerful bite force, capable of crushing bone.\n- Forelegs are longer than hind legs, giving them a sloping back.\n- Complex social systems.",
            "population": "- Spotted hyenas are abundant (Least Concern), but other species like the Striped hyena are Near Threatened.",
            "preservation": "- Dispel myths and educate communities to reduce human-hyena conflict.\n- Protect large savanna ecosystems.\n- Monitor populations threatened by persecution."
        }
    },
    "Kangaroo": {
        "title": "Large Australian Marsupial",
        "details": {
            "features": "- Powerful hind legs for hopping, and a long, muscular tail for balance.\n- Females have a pouch (marsupium) to carry their young (joeys).",
            "population": "- Abundant (Least Concern), with populations of some species in the tens of millions.",
            "preservation": "- Population is managed through regulated harvesting programs.\n- Protect habitats from overgrazing by livestock and urban sprawl."
        }
    },
    "Koala": {
        "title": "Arboreal Australian Marsupial",
        "details": {
            "features": "- Specialized diet of eucalyptus leaves.\n- Large, furry ears, a stout body, and no tail.\n- Mostly sedentary, sleeping up to 20 hours a day.",
            "population": "- Endangered. Populations have been devastated by habitat loss, disease, and bushfires, with estimates varying widely.",
            "preservation": "- Protect and restore eucalyptus forest habitats.\n- Create safe corridors for koalas to move between trees.\n- Support koala hospitals and disease research."
        }
    },
    "Leopard": {
        "title": "Adaptable Big Cat",
        "details": {
            "features": "- Known for its beautiful rosette-patterned coat for camouflage.\n- Incredibly strong, able to haul heavy prey up into trees.",
            "population": "- Vulnerable. They have the largest range of any big cat but are declining due to habitat loss and intense persecution.",
            "preservation": "- Implement strong anti-poaching measures (especially for their skins).\n- Promote coexistence with local communities to reduce conflict.\n- Protect habitat corridors."
        }
    },
    "Lion": {
        "title": "Social Predator & Tourism Asset",
        "details": {
            "features": "- The only cat to live in social groups (prides).\n- Males are distinguished by their prominent mane.",
            "population": "- Vulnerable, with only about 20,000 remaining in the wild. They have disappeared from over 90% of their historic range.",
            "preservation": "- Protect large, connected conservation areas.\n- Mitigate human-lion conflict with measures like predator-proof enclosures for livestock.\n- Combat poaching and the illegal trade in lion parts."
        }
    },
    "Mouse": {
        "title": "Small Rodent",
        "details": {
            "features": "- Small body, pointed snout, large rounded ears, and a long, scaly tail.\n- Prolific breeders.",
            "population": "- Extremely abundant and widespread (Least Concern).",
            "preservation": "- Not a conservation target. Focus is on pest control and their use as a model organism in scientific research."
        }
    },
    "Okapi": {
        "title": "Elusive Forest Giraffid",
        "details": {
            "features": "- The only living relative of the giraffe.\n- Has a velvety, reddish-brown coat with distinctive zebra-like stripes on its legs.",
            "population": "- Endangered, with an estimated 10,000-25,000 remaining in a small, dense rainforest habitat.",
            "preservation": "- Protect the Ituri Forest in the Democratic Republic of Congo.\n- Combat illegal mining, logging, and poaching in their habitat.\n- Support community conservation initiatives."
        }
    },
    "Orangutan": {
        "title": "Arboreal Great Ape of Asia",
        "details": {
            "features": "- The world's largest tree-dwelling animal, with long arms for swinging (brachiation).\n- Males develop large cheek pads (flanges).",
            "population": "- Critically Endangered. All three species have suffered sharp declines due to deforestation.",
            "preservation": "- Halt deforestation for palm oil plantations by promoting sustainable palm oil.\n- Protect and reforest peat-swamp forests.\n- Rescue and rehabilitate orphaned orangutans."
        }
    },
    "Otter": {
        "title": "Semi-Aquatic Playful Carnivore",
        "details": {
            "features": "- Long, streamlined body with short legs and webbed feet for swimming.\n- Dense, waterproof fur for insulation.",
            "population": "- Many of the 13 species are Near Threatened or Endangered due to water pollution and habitat loss.",
            "preservation": "- Restore and protect wetland, river, and coastal habitats.\n- Reduce chemical and plastic pollution in waterways.\n- Reintroduce otters to their former habitats where viable."
        }
    },
    "Ox": {
        "title": "Domesticated Draft Animal",
        "details": {
            "features": "- An ox is a bovine (typically a bull) trained as a draft animal.\n- Known for their strength, stamina, and docile nature.",
            "population": "- Abundant as a domesticated animal. Wild oxen, like the Gaur (Vulnerable), are a conservation concern.",
            "preservation": "- For wild relatives, protect forest and grassland habitats from human encroachment and poaching."
        }
    },
    "Panda": {
        "title": "Conservation Icon & Bamboo Specialist",
        "details": {
            "features": "- Distinctive black-and-white coat.\n- Specialized diet consisting almost entirely of bamboo.\n- Has a 'pseudo-thumb' (a modified wrist bone) to help grip bamboo.",
            "population": "- Vulnerable, a conservation success that upgraded them from Endangered. Around 1,800 live in the wild.",
            "preservation": "- Protect and expand their mountain forest habitat in China.\n- Create bamboo corridors to connect isolated populations.\n- Support captive breeding and reintroduction programs."
        }
    },
    "Pig": {
        "title": "Domesticated Suid",
        "details": {
            "features": "- Intelligent and social animal with a snout adapted for digging (rooting).\n- Domesticated for meat (pork).",
            "population": "- Abundant globally as livestock.",
            "preservation": "- Focus on the conservation of rare and heritage breeds.\n- Manage feral pig populations to protect native ecosystems."
        }
    },
    "Porcupine": {
        "title": "Quilled Rodent",
        "details": {
            "features": "- Covered in a coat of sharp spines, or quills, used for defense.\n- Herbivorous and primarily nocturnal.",
            "population": "- Most species are common and widespread (Least Concern).",
            "preservation": "- Generally not a conservation focus, but their habitats (forests and deserts) should be protected for overall biodiversity."
        }
    },
    "Possum": {
        "title": "Nocturnal Marsupial",
        "details": {
            "features": "- Marsupials native to Australia and surrounding islands (Opossums are from the Americas).\n- Often have a prehensile tail for gripping branches.",
            "population": "- Varies widely. The Common Brushtail Possum is abundant (and invasive in New Zealand), while others, like the Leadbeater's Possum, are Critically Endangered.",
            "preservation": "- Protect old-growth forests with hollow trees for nesting.\n- Control invasive predators like cats and foxes.\n- Implement captive breeding for critically endangered species."
        }
    },
    "Raccoon": {
        "title": "Adaptable Nocturnal Omnivore",
        "details": {
            "features": "- Distinctive black mask across its eyes and a ringed tail.\n- Highly dexterous front paws, capable of manipulating objects.",
            "population": "- Abundant and expanding its range (Least Concern).",
            "preservation": "- Not a conservation target. Management focuses on public education to reduce human-raccoon conflict in urban areas and control of rabies."
        }
    },
    "Rat": {
        "title": "Ubiquitous Rodent",
        "details": {
            "features": "- Medium-sized, long-tailed rodents.\n- Highly adaptable and intelligent.",
            "population": "- Extremely abundant and widespread (Least Concern). Brown and Black rats are highly invasive.",
            "preservation": "- Eradication programs are critical on islands to protect native birds and reptiles from predation. Not a conservation target otherwise."
        }
    },
    "Reindeer": {
        "title": "Arctic and Subarctic Deer",
        "details": {
            "features": "- Also known as Caribou in North America.\n- The only deer species where both sexes grow antlers.\n- Large, crescent-shaped hooves that act as snowshoes.",
            "population": "- Vulnerable. Some populations are declining sharply due to climate change affecting their food sources and habitat.",
            "preservation": "- Protect calving grounds from industrial development.\n- Mitigate the impacts of climate change on the Arctic tundra.\n- Work with indigenous communities who depend on them."
        }
    },
    "Rhinoceros": {
        "title": "Large, Horned Herbivore",
        "details": {
            "features": "- Large, thick-skinned mammal with one or two horns on its snout.\n- Horns are made of keratin, not bone.",
            "population": "- Critically Endangered. Black, Javan, and Sumatran rhinos have extremely low numbers. White rhinos are Near Threatened.",
            "preservation": "- Implement intensive, military-style anti-poaching patrols.\n- De-horning programs and translocation to secure locations.\n- Disrupt international trafficking networks for rhino horn."
        }
    },
    "Sheep": {
        "title": "Domesticated Ruminant",
        "details": {
            "features": "- Typically have a fleece of crimped hair called wool.\n- Known for strong flocking behavior.",
            "population": "- Abundant globally as livestock. Wild sheep species, like the Bighorn Sheep, are a conservation focus.",
            "preservation": "- Protect wild sheep from disease transmission from domestic livestock.\n- Conserve mountain habitats and migration routes for wild species."
        }
    },
    "Squirrel": {
        "title": "Agile Rodent",
        "details": {
            "features": "- Slender body with a long, bushy tail.\n- Known for burying nuts and seeds, which aids in forest regeneration.",
            "population": "- Most species are abundant (Least Concern). Some, like the Red Squirrel in the UK, are threatened by the invasive Grey Squirrel.",
            "preservation": "- Protect forest and woodland habitats.\n- Manage invasive squirrel species to protect native ones.\n- Maintain mature trees that provide food and nesting sites."
        }
    },
    "Tiger": {
        "title": "Apex Predator & Endangered Species",
        "details": {
            "features": "- The largest cat species, with distinctive vertical stripes for camouflage.\n- Powerful solitary hunter.",
            "population": "- Endangered. After a century of decline, wild tiger numbers are slowly rising, with an estimate of around 4,500.",
            "preservation": "- Zero-tolerance anti-poaching patrols.\n- Protect and connect large forest landscapes.\n- Work with local communities to mitigate human-tiger conflict."
        }
    },
    "Whale": {
        "title": "Large Marine Mammal",
        "details": {
            "features": "- Fully aquatic mammals, including the largest animal on Earth, the Blue Whale.\n- Breathe air through a blowhole.",
            "population": "- Many species are recovering after being hunted to near-extinction. Blue, Fin, and Right whales are still Endangered.",
            "preservation": "- Uphold the international ban on commercial whaling.\n- Reduce ship strikes and entanglement in fishing gear.\n- Combat ocean noise pollution and protect critical feeding and breeding grounds."
        }
    },
    "Wolf": {
        "title": "Apex Canid Predator",
        "details": {
            "features": "- Highly intelligent and social, living and hunting in complex packs.\n- Ancestor of the domestic dog.",
            "population": "- Recovering in parts of their historic range but still persecuted. Global population is stable (Least Concern), but many local populations are endangered.",
            "preservation": "- Reintroduce wolves to ecosystems where they were extirpated.\n- Promote coexistence with livestock ranchers through non-lethal deterrents.\n- Protect wilderness areas and corridors."
        }
    },
    "Wombat": {
        "title": "Burrowing Australian Marsupial",
        "details": {
            "features": "- Stocky, muscular marsupial with rodent-like teeth.\n- Digs extensive burrow systems and produces distinctive cube-shaped feces.",
            "population": "- Common Wombat is Least Concern, but the Northern Hairy-nosed Wombat is one of the rarest mammals on Earth (Critically Endangered).",
            "preservation": "- Protect their grassland and woodland habitats.\n- Implement intensive recovery programs for the Northern Hairy-nosed Wombat, including predator-proof fences."
        }
    },
    "Zebra": {
        "title": "Striped African Equid",
        "details": {
            "features": "- Distinctive black-and-white striped coat, unique to each individual.\n- Social animals living in herds.",
            "population": "- Plains Zebra are numerous, but Grevy's Zebra is Endangered (fewer than 2,500) and Mountain Zebra is Vulnerable.",
            "preservation": "- Protect grazing lands from agricultural expansion.\n- Secure water sources, which are critical in their arid habitats.\n- Combat poaching for their skins and manage competition with livestock."
        }
    },
    # --- BIRDS ---
    "Crow": {
        "title": "Intelligent Black Bird",
        "details": {
            "features": "- Large, all-black bird known for its intelligence, problem-solving abilities, and loud 'caw'.",
            "population": "- Abundant and widespread (Least Concern).",
            "preservation": "- Not a conservation target. Often managed as a pest in agricultural areas."
        }
    },
    "Duck": {
        "title": "Aquatic Bird (Waterfowl)",
        "details": {
            "features": "- Broad, flat bill and webbed feet for swimming.\n- Feathers are highly waterproof.",
            "population": "- Most species are abundant, but some, like the White-winged Duck, are Endangered.",
            "preservation": "- Conserve and restore wetland habitats (marshes, ponds, rivers).\n- Manage sustainable hunting programs.\n- Monitor for avian influenza."
        }
    },
    "Eagle": {
        "title": "Large Bird of Prey",
        "details": {
            "features": "- Large, powerfully built with a heavy head and beak.\n- Exceptional eyesight (keen vision) for spotting prey from a distance.",
            "population": "- Many species, like the Bald Eagle, have recovered thanks to conservation but some, like the Philippine Eagle, are Critically Endangered.",
            "preservation": "- Ban harmful pesticides like DDT.\n- Protect large, mature trees for nesting.\n- Reduce lead poisoning from ammunition."
        }
    },
    "Flamingo": {
        "title": "Unique Filter-Feeding Wader",
        "details": {
            "features": "- Long legs and neck, and a distinctive downward-bent bill for filter-feeding.\n- Pink plumage comes from pigments in their algae and crustacean diet.",
            "population": "- Most species are stable, but the Andean Flamingo is Vulnerable due to mining and water extraction in their high-altitude wetlands.",
            "preservation": "- Protect their specialized wetland and salt flat habitats from pollution and water diversion.\n- Minimize human disturbance at nesting colonies."
        }
    },
    "Goose": {
        "title": "Migratory Waterfowl",
        "details": {
            "features": "- Large water bird, smaller than a swan but larger than a duck.\n- Known for migrating long distances in a V-formation.",
            "population": "- Many species, like the Canada Goose, are abundant. Others, like the Red-breasted Goose, are Vulnerable.",
            "preservation": "- Protect wetland staging areas along their migratory routes.\n- Manage sustainable hunting.\n- Address threats to specific endangered populations."
        }
    },
    "Hornbill": {
        "title": "Bird with a 'Casque'",
        "details": {
            "features": "- Characterized by a long, down-curved bill which is often brightly colored and has a casque on the upper mandible.\n- Unique nesting behavior where the female is sealed in a tree cavity.",
            "population": "- Many species are threatened by deforestation, as they require large, mature trees for nesting.",
            "preservation": "- Protect old-growth tropical forests.\n- Combat poaching for their casques (sometimes called 'ivory').\n- Provide artificial nest boxes in reforested areas."
        }
    },
    "Hummingbird": {
        "title": "Tiny, Agile Nectarivore",
        "details": {
            "features": "- The smallest birds, capable of hovering and flying backward.\n- Extremely rapid wing beats.\n- Iridescent plumage.",
            "population": "- Most are stable, but some species with very small ranges are Critically Endangered.",
            "preservation": "- Protect their forest habitats, especially in Central and South America.\n- Encourage planting of native nectar-producing flowers.\n- Address threats from climate change affecting flowering seasons."
        }
    },
    "Owl": {
        "title": "Nocturnal Bird of Prey",
        "details": {
            "features": "- Forward-facing eyes, a facial disc, and binocular vision.\n- Capable of silent flight due to serrated wing feathers.\n- Can rotate its neck up to 270 degrees.",
            "population": "- Many species are widespread, but some, like the Snowy Owl and Blakiston's Fish Owl, are Vulnerable or Endangered due to habitat loss.",
            "preservation": "- Protect mature forests and grasslands.\n- Reduce rodenticide use, which can poison owls.\n- Install nesting boxes for species like the Barn Owl."
        }
    },
    "Parrot": {
        "title": "Intelligent & Colorful Bird",
        "details": {
            "features": "- Strong, curved beak for cracking nuts and seeds.\n- Zygodactyl feet (two toes forward, two back) for climbing.\n- Highly intelligent and capable of mimicking human speech.",
            "population": "- Nearly one-third of all parrot species are threatened with extinction, making them one of the most at-risk bird groups.",
            "preservation": "- Enforce strict laws against the illegal pet trade.\n- Protect tropical and subtropical forests.\n- Support captive breeding and reintroduction programs for species like the Kakapo and Spix's Macaw."
        }
    },
    "Pelecaniformes": {
        "title": "Order of Water Birds (e.g., Pelicans)",
        "details": {
            "features": "- This is a taxonomic order, with Pelicans being a key example.\n- Pelicans have a distinctive throat pouch (gular pouch) for catching fish.",
            "population": "- Most pelican species have recovered from pesticide threats and are stable, but some are still a conservation concern.",
            "preservation": "- Protect coastal and inland wetland breeding colonies from disturbance.\n- Reduce plastic pollution and entanglement in fishing gear."
        }
    },
    "Penguin": {
        "title": "Flightless Seabird of the Southern Hemisphere",
        "details": {
            "features": "- Flightless, with wings adapted into flippers for swimming.\n- Counter-shaded (black back, white front) for camouflage in the water.",
            "population": "- Many populations are declining. The Emperor Penguin and African Penguin are Vulnerable and Endangered, respectively.",
            "preservation": "- Combat climate change, which is melting sea ice (critical for some species) and affecting food supply.\n- Establish large Marine Protected Areas (MPAs).\n- Reduce overfishing of their primary food sources."
        }
    },
    "Pigeon": {
        "title": "Common Urban Bird",
        "details": {
            "features": "- Stout-bodied birds with short necks and short, slender bills.\n- The common Rock Dove (city pigeon) is highly adapted to urban life.",
            "population": "- Extremely abundant and widespread (Least Concern). However, many wild pigeon and dove species are threatened.",
            "preservation": "- The Rock Dove requires no preservation.\n- Conservation efforts are focused on endangered species like the Pink Pigeon or Tooth-billed Pigeon."
        }
    },
    "Sandpiper": {
        "title": "Wading Shorebird",
        "details": {
            "features": "- Long body, long legs, and a narrow bill used for probing in sand and mud for invertebrates.\n- Often seen in flocks along coastlines.",
            "population": "- Many species are undergoing steep population declines due to habitat loss along their long migratory routes.",
            "preservation": "- Protect and restore coastal wetlands, mudflats, and beaches.\n- Minimize human disturbance at key stopover sites during migration.\n- Address coastal development and sea-level rise."
        }
    },
    "Sparrow": {
        "title": "Small Seed-Eating Bird",
        "details": {
            "features": "- Small, plump, brown-grey birds with short tails and stout beaks for eating seeds.\n- Highly social.",
            "population": "- The House Sparrow is abundant globally, but many native sparrow populations in North America and Europe are in decline.",
            "preservation": "- Preserve native grasslands and shrublands.\n- Encourage wildlife-friendly farming practices that provide winter food and nesting habitat."
        }
    },
    "Swan": {
        "title": "Graceful Waterfowl",
        "details": {
            "features": "- The largest waterfowl, known for their long, gracefully curved necks.\n- Typically mate for life.",
            "population": "- Most species are stable (Least Concern), including the Mute Swan and Tundra Swan.",
            "preservation": "- Protect wetland habitats from pollution and drainage.\n- Reduce lead poisoning from fishing tackle and ammunition."
        }
    },
    "Turkey": {
        "title": "Large Game Bird",
        "details": {
            "features": "- Large, plump bird, with males (gobblers) known for their fan-like tail, wattle, and snood.\n- A ground-dwelling bird capable of short flights.",
            "population": "- A conservation success story in North America, where wild turkey populations have rebounded and are abundant (Least Concern).",
            "preservation": "- Habitat management through controlled burns and forest thinning.\n- Maintain sustainable hunting programs."
        }
    },
    "Woodpecker": {
        "title": "Forest Bird Adapted for Pecking",
        "details": {
            "features": "- Strong beak for drilling into wood, and a very long, barbed tongue for extracting insects.\n- Stiff tail feathers to prop themselves up against tree trunks.",
            "population": "- Most are stable, but species dependent on old-growth forests, like the Ivory-billed Woodpecker (likely extinct), are highly endangered.",
            "preservation": "- Protect mature and dead standing trees (snags), which are critical for nesting and feeding.\n- Promote sustainable forestry practices."
        }
    },
    # --- REPTILES / AMPHIBIANS ---
    "Lizard": {
        "title": "Diverse Group of Reptiles",
        "details": {
            "features": "- Typically have four legs, external ears, and movable eyelids (distinguishing them from snakes).\n- A vast and diverse group including geckos, iguanas, and chameleons.",
            "population": "- Highly variable. Many are common, but numerous species, especially island endemics, are Critically Endangered.",
            "preservation": "- Protect habitats from urbanization and agriculture.\n- Control invasive species that prey on them.\n- Combat the illegal pet trade."
        }
    },
    "Snake": {
        "title": "Legless Reptile",
        "details": {
            "features": "- Elongated, legless, carnivorous reptiles.\n- Forked tongue used to 'smell' the air.\n- Can swallow prey much larger than their head.",
            "population": "- Many species are common, but some are threatened by habitat destruction and persecution by humans.",
            "preservation": "- Educate the public to reduce fear-based killing.\n- Protect their specific habitats, from forests to wetlands.\n- Combat the illegal trade for skin and pets."
        }
    },
    "Turtle": {
        "title": "Reptile with a Protective Shell",
        "details": {
            "features": "- Characterized by a special bony or cartilaginous shell developed from their ribs.\n- Includes terrestrial (tortoises), freshwater, and marine species.",
            "population": "- Over half of all turtle and tortoise species are threatened with extinction, making them one of the most endangered vertebrate groups.",
            "preservation": "- Protect nesting beaches for sea turtles.\n- Reduce plastic pollution and bycatch in fisheries.\n- Combat the illegal trade for food, shells, and pets."
        }
    },
    # --- INSECTS / ARACHNIDS ---
    "Bee": {
        "title": "Essential Pollinator",
        "details": {
            "features": "- Flying insect known for its role in pollination and for producing honey and beeswax (honey bees).\n- Hairy bodies are adapted for collecting pollen.",
            "population": "- Many species, including honey bees and numerous wild bee species, are facing serious declines globally.",
            "preservation": "- Ban or reduce the use of harmful neonicotinoid pesticides.\n- Plant native wildflowers to provide food.\n- Protect natural habitats like meadows and forests."
        }
    },
    "Beetle": {
        "title": "Most Diverse Order of Insects",
        "details": {
            "features": "- Characterized by a hard pair of forewings called elytra, which protect the flight wings underneath.\n- Occupy nearly every habitat on Earth.",
            "population": "- The most species-rich order of animals. Most are abundant, but some specialized species are threatened by habitat loss.",
            "preservation": "- Protect ancient forests with dead wood, which is a critical habitat for many beetle species.\n- Reduce pesticide use."
        }
    },
    "Butterfly": {
        "title": "Indicator of a Healthy Environment",
        "details": {
            "features": "- Large, often brightly colored wings.\n- Undergo a complete metamorphosis: egg, larva (caterpillar), pupa (chrysalis), and adult.",
            "population": "- Many species are in decline due to habitat loss and climate change. The Monarch butterfly is a well-known endangered example.",
            "preservation": "- Plant native host plants for caterpillars (e.g., milkweed for Monarchs).\n- Create and protect wildflower meadows.\n- Reduce pesticide use."
        }
    },
    "Caterpillar": {
        "title": "Larval Stage of Butterflies and Moths",
        "details": {
            "features": "- The larval stage, characterized by a segmented, worm-like body.\n- Voracious eaters, primarily feeding on plant leaves.",
            "population": "- Tied directly to the population status of their adult butterfly/moth counterparts.",
            "preservation": "- Preservation efforts are the same as for butterflies and moths: protect host plants and reduce pesticides."
        }
    },
    "Cockroach": {
        "title": "Hardy Scavenging Insect",
        "details": {
            "features": "- Broad, flattened body and long antennae.\n- Known for their extreme resilience and ability to thrive in human environments.",
            "population": "- Extremely abundant. Only a few of the 4,600 species are considered pests.",
            "preservation": "- Not a conservation target. Tropical, non-pest species are an important part of forest ecosystems as decomposers."
        }
    },
    "Dragonfly": {
        "title": "Agile Aerial Insect Predator",
        "details": {
            "features": "- Large multifaceted eyes, two pairs of strong, transparent wings, and an elongated body.\n- Skilled fliers, able to hover and fly at high speeds.",
            "population": "- Generally common, but species dependent on pristine wetland habitats are threatened by pollution and drainage.",
            "preservation": "- Protect and restore unpolluted wetlands, ponds, and streams.\n- Monitor water quality."
        }
    },
    "Fly": {
        "title": "Common Pest & Disease Vector",
        "details": {
            "features": "- Have only one pair of wings for flight (the hind pair are reduced to halteres for balance).\n- Sponging or piercing mouthparts.",
            "population": "- Extremely abundant (Least Concern).",
            "preservation": "- Not a conservation focus. Some species are important pollinators, but management is often aimed at pest control for public health."
        }
    },
    "Grasshopper": {
        "title": "Jumping Herbivorous Insect",
        "details": {
            "features": "- Large hind legs adapted for jumping.\n- Produce sound (stridulation) by rubbing their legs against their wings.",
            "population": "- Most species are abundant, but can have dramatic population swings. Can be major agricultural pests (locusts).",
            "preservation": "- Preserve native prairie and grassland habitats, as many species are specialized to these environments."
        }
    },
    "Ladybugs": {
        "title": "Beneficial Beetle (Ladybird)",
        "details": {
            "features": "- Small, often brightly colored and spotted dome-shaped beetles.\n- Widely considered beneficial as they prey on aphids and other garden pests.",
            "population": "- Most species are common, but some native species are threatened by invasive ones (like the Asian Lady Beetle).",
            "preservation": "- Reduce pesticide use to support their populations.\n- Encourage planting of native species that support aphid populations as a food source."
        }
    },
    "Mosquito": {
        "title": "Disease-Transmitting Insect",
        "details": {
            "features": "- Slender body, long legs, and a proboscis for feeding.\n- Females of most species feed on blood to get protein for their eggs.",
            "population": "- Extremely abundant (Least Concern).",
            "preservation": "- Not a conservation target. Global health efforts are focused on controlling mosquito populations to prevent the spread of diseases like malaria, dengue, and Zika."
        }
    },
    "Moth": {
        "title": "Nocturnal Pollinator",
        "details": {
            "features": "- Similar to butterflies but typically have stout bodies, feathery antennae, and are nocturnal.\n- Important pollinators for night-blooming flowers.",
            "population": "- Many species are in decline due to habitat loss and light pollution, which disrupts their navigation and reproduction.",
            "preservation": "- Reduce nighttime light pollution.\n- Plant native plants that are hosts for their caterpillars.\n- Protect wild habitats."
        }
    },
    # --- MARINE / AQUATIC ---
    "Crab": {
        "title": "Decapod Crustacean",
        "details": {
            "features": "- Have a thick exoskeleton (carapace) and a single pair of claws (chelae).\n- Walk sideways.",
            "population": "- Many species are abundant and form the basis of major fisheries. Some are threatened by habitat destruction (e.g., mangrove loss).",
            "preservation": "- Protect coastal habitats like mangroves and coral reefs.\n- Implement sustainable fishing regulations to prevent overharvesting."
        }
    },
    "Goldfish": {
        "title": "Domesticated Carp",
        "details": {
            "features": "- A domesticated version of a wild carp species.\n- One of the earliest fish to be domesticated.",
            "population": "- Abundant in captivity. They are a highly destructive invasive species when released into the wild.",
            "preservation": "- Public education is key to prevent their release into natural ponds and lakes where they harm native ecosystems."
        }
    },
    "Jellyfish": {
        "title": "Gelatinous Marine Animal",
        "details": {
            "features": "- Soft, bell-shaped body with stinging tentacles.\n- Lack a brain, heart, or bones.",
            "population": "- Populations (blooms) can fluctuate dramatically and may be increasing in some areas due to climate change and overfishing of their predators.",
            "preservation": "- Not a direct conservation target. Their blooms are monitored as an indicator of changes in ocean ecosystems."
        }
    },
    "Lobster": {
        "title": "Large Marine Crustacean",
        "details": {
            "features": "- Long body with a muscular tail, five pairs of legs, the first of which are large claws.\n- Can live for a very long time.",
            "population": "- Heavily managed for commercial fishing. Some populations are healthy due to strict regulations, while others have been overfished.",
            "preservation": "- Enforce sustainable fishing practices, including size limits and trap restrictions.\n- Protect marine nursery habitats."
        }
    },
    "Octopus": {
        "title": "Highly Intelligent Cephalopod",
        "details": {
            "features": "- Eight arms with suckers, a soft body, and a sharp beak.\n- Masters of camouflage with incredible problem-solving abilities.",
            "population": "- Generally not considered threatened, but populations are difficult to assess. They are sensitive to changes in ocean acidity and temperature.",
            "preservation": "- Protect their marine habitats, especially coral reefs and seabeds.\n- Promote sustainable fishing practices."
        }
    },
    "Oyster": {
        "title": "Filter-Feeding Bivalve Mollusc",
        "details": {
            "features": "- Has a rough, irregular shell.\n- A keystone species that filters water and builds reefs that provide habitat for other animals.",
            "population": "- Wild oyster populations have been decimated globally (over 85% lost) due to overharvesting, pollution, and disease.",
            "preservation": "- Large-scale restoration projects to rebuild oyster reefs.\n- Improve water quality by reducing nutrient runoff.\n- Support sustainable oyster aquaculture."
        }
    },
    "Seahorse": {
        "title": "Unique Upright-Swimming Fish",
        "details": {
            "features": "- Swims upright, has a prehensile tail to grip seagrass, and a horse-like head.\n- The male carries the eggs and gives birth to live young.",
            "population": "- Many species are Vulnerable due to overharvesting for traditional medicine and the pet trade, as well as habitat destruction.",
            "preservation": "- Protect and restore seagrass beds and mangrove habitats.\n- Ban destructive fishing practices like bottom trawling.\n- Enforce trade regulations."
        }
    },
    "Seal": {
        "title": "Fin-Footed Marine Mammal (Pinniped)",
        "details": {
            "features": "- Streamlined body and four flippers adapted for aquatic life.\n- A layer of blubber for insulation in cold water.",
            "population": "- Many species, like the Grey Seal, have recovered well under protection. Others, like the Monk Seal, are Critically Endangered.",
            "preservation": "- Protect haul-out sites and breeding colonies from human disturbance.\n- Reduce entanglement in marine debris and fishing gear.\n- Address climate change impacts on their sea-ice habitats."
        }
    },
    "Shark": {
        "title": "Apex Marine Predator",
        "details": {
            "features": "- Cartilaginous skeleton (not bone).\n- Highly streamlined body and keen senses, especially smell.",
            "population": "- Over one-third of all shark and ray species are now threatened with extinction due to overfishing.",
            "preservation": "- Ban shark finning and implement strict fishing quotas.\n- Establish shark sanctuaries and protect nursery grounds.\n- Educate the public to change the perception of sharks."
        }
    },
    "Squid": {
        "title": "Fast-Swimming Cephalopod",
        "details": {
            "features": "- Has two long tentacles and eight arms, a distinct head, and a torpedo-shaped body.\n- Can change color rapidly and squirt ink for defense.",
            "population": "- Most species are not considered threatened and form the basis of major global fisheries. They have short, productive life cycles.",
            "preservation": "- Implement sustainable management of fisheries to prevent overexploitation."
        }
    },
    "Starfish": {
        "title": "Echinoderm (Sea Star)",
        "details": {
            "features": "- Typically has a central disc and five arms, though some species have more.\n- Can regenerate lost arms.",
            "population": "- Generally common, but have suffered massive die-offs in recent years from Sea Star Wasting Disease, linked to warming waters.",
            "preservation": "- Combat climate change and ocean warming.\n- Monitor for disease outbreaks and protect marine habitats."
        }
    },
    "Default": {
        "title": "Information Not Available",
        "details": {
            "features": "No specific feature information is in the knowledge base yet.",
            "population": "Population status for this species has not been added.",
            "preservation": "General conservation advice includes habitat protection and reducing human-wildlife conflict."
        }
    }
}